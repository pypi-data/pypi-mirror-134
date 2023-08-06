import os
import tempfile
from pathlib import Path
from typing import Final, Optional, Sequence, Union

import scp
from scp import SCPClient

from ufrc.exc import NoUFRCConnectionException
from ufrc.sbatch import SBatchFile
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
        ssh.connect(self.server, username=username, password=password)
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

    def run(self, command: str) -> SSHResponse:
        if self._ssh_client is None:
            raise NoUFRCConnectionException(
                "Use .connect(username, password) before .run"
            )

        _, ssh_stdout, ssh_stderr = self._ssh_client.exec_command(command)
        return SSHResponse(
            stdout=ssh_stdout.read().decode(),
            stderr=ssh_stderr.read().decode(),
        )

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

    # TODO: run python code directly
