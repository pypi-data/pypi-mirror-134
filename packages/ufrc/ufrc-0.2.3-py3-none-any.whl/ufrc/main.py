import os
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Final, Optional, Sequence, Union, List

import paramiko
import scp
from scp import SCPClient

from ufrc.exc import NoUFRCConnectionException
from ufrc.sbatch import SBatchFile
from ufrc.squeue.model import SQueueResponse, Job
from ufrc.ssh.client import SSHClient
from ufrc.ssh.response import SSHResponse

SERVER: Final[str] = "hpg.rc.ufl.edu"


class UFRC:
    def __init__(self, server: str = SERVER):
        self.server = server

        self._ssh_client: Optional[SSHClient] = None
        self._scp_client: Optional[SCPClient] = None

    def connect(self, username: str, password: str):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server, username=username, password=password)
        channel = ssh.invoke_shell()
        self._stdin = channel.makefile("wb")
        self._stdout = channel.makefile("r")
        self._ssh_client = ssh
        self._scp_client = SCPClient(ssh.get_transport())

    def disconnect(self):
        self._ssh_client.close()
        del self._ssh_client
        del self._scp_client
        self._ssh_client = None
        self._scp_client = None

    @property
    def is_connected(self) -> bool:
        return self._ssh_client is not None

    def _execute_command(self, cmd: str) -> SSHResponse:
        # Adapted from https://stackoverflow.com/a/36948840/6276321
        cmd = cmd.strip("\n")
        self._stdin.write(cmd + "\n")
        finish = "end of stdOUT buffer. finished with exit status"
        echo_cmd = "echo {} $?".format(finish)
        self._stdin.write(echo_cmd + "\n")
        shin = self._stdin
        self._stdin.flush()

        shout: List[str] = []
        sherr: List[str] = []
        exit_status = 0
        for line in self._stdout:
            if str(line).startswith(cmd) or str(line).startswith(echo_cmd):
                # up for now filled with shell junk from stdin
                shout = []
            elif str(line).startswith(finish):
                # our finish command ends with the exit status
                exit_status = int(str(line).rsplit(maxsplit=1)[1])
                if exit_status:
                    # stderr is combined with stdout.
                    # thus, swap sherr with shout in a case of failure.
                    sherr = shout
                    shout = []
                break
            else:
                # get rid of 'coloring and formatting' special characters
                shout.append(
                    re.compile(r"(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]")
                    .sub("", line)
                    .replace("\b", "")
                    .replace("\r", "")
                )

        # first and last lines of shout/sherr contain a prompt
        if shout and echo_cmd in shout[-1]:
            shout.pop()
        if shout and cmd in shout[0]:
            shout.pop(0)
        if sherr and echo_cmd in sherr[-1]:
            sherr.pop()
        if sherr and cmd in sherr[0]:
            sherr.pop(0)

        return SSHResponse(stdout="\n".join(shout), stderr="\n".join(sherr))

    def run(self, command: str) -> SSHResponse:
        if self._ssh_client is None:
            raise NoUFRCConnectionException(
                "Use .connect(username, password) before .run"
            )

        return self._execute_command(command)

    def put(
        self,
        files: Union[str, Sequence[str]],
        to_path: str = ".",
        recursive=False,
        preserve_times=False,
    ):
        if self._scp_client is None:
            raise NoUFRCConnectionException(
                "Use .connect(username, password) before .put"
            )

        self._scp_client.put(
            files, to_path, recursive=recursive, preserve_times=preserve_times
        )

    def put_sbatch(
        self, sbatch: SBatchFile, file_name: str = "my_job.sbatch", to_path: str = "."
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            out_path = Path(temp_dir) / file_name
            out_path.write_text(sbatch.contents)
            self.put(str(out_path), to_path=to_path)

    def get(
        self,
        remote_path: str,
        local_path: str = "",
        recursive=False,
        preserve_times=False,
    ):
        if self._scp_client is None:
            raise NoUFRCConnectionException(
                "Use .connect(username, password) before .get"
            )

        self._scp_client.get(
            remote_path, local_path, recursive=recursive, preserve_times=preserve_times
        )

    def job_status(
        self,
        group_name: Optional[str] = None,
        user_id: Optional[int] = None,
        job_name: Optional[str] = None,
    ) -> SQueueResponse:
        ssh_response = self.run("squeue --json")
        json_idx = ssh_response.stdout.find("{")
        json_input = ssh_response.stdout[json_idx:] + "}"
        squeue_response = SQueueResponse.parse_raw(json_input)
        if not group_name:
            return squeue_response
        new_jobs: List[Job] = []
        for job in squeue_response.jobs:
            include_job = True
            if group_name and job.account != group_name and job.qos != group_name:
                include_job = False
            if include_job and user_id and job.user_id != user_id:
                include_job = False
            if include_job and job_name and job.name != job_name:
                include_job = False
            if include_job:
                new_jobs.append(job)
        return squeue_response.copy(update=dict(jobs=new_jobs))

    def cancel_job_by_id(self, job_id: int) -> SSHResponse:
        return self.run(f"scancel {job_id}")

    def cancel_jobs_by_lookup(
        self,
        group_name: Optional[str] = None,
        user_id: Optional[int] = None,
        job_name: Optional[str] = None,
    ) -> SSHResponse:
        job_status = self.job_status(
            group_name=group_name, user_id=user_id, job_name=job_name
        )
        full_response = SSHResponse(stdout="", stderr="")
        for job in job_status.jobs:
            print(
                f"Cancelling job {job.job_id}: {job.name} running in group {group_name} under user {user_id}"
            )
            response = self.cancel_job_by_id(job.job_id)
            print(response)
            full_response += response
        return full_response

    # TODO: run python code directly
