from typing import Final, Optional

from ufrc.exc import NoUFRCConnectionException
from ufrc.ssh.client import SSHClient
from ufrc.ssh.response import SSHResponse

SERVER: Final[str] = "hpg.rc.ufl.edu"


class UFRC:
    def __init__(self, server: str = SERVER):
        self.server = server

        self._ssh_client: Optional[SSHClient] = None

    def connect(self, username: str, password: str):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(self.server, username=username, password=password)
        self._ssh_client = ssh

    def disconnect(self):
        self._ssh_client.close()
        del self._ssh_client
        self._ssh_client = None

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

    # TODO: run python code directly