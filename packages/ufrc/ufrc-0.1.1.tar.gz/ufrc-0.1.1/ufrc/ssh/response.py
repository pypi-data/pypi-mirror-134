from dataclasses import dataclass


@dataclass(frozen=True)
class SSHResponse:
    stdout: str
    stderr: str
