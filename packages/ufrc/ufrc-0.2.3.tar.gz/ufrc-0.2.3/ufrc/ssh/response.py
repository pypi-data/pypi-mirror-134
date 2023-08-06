from dataclasses import dataclass


@dataclass(frozen=True)
class SSHResponse:
    stdout: str
    stderr: str

    def __add__(self, other) -> "SSHResponse":
        try:
            new_stdout = self.stdout + "\n" + other.stdout
            new_stderr = self.stderr + "\n" + other.stderr
        except AttributeError:
            raise ValueError("can only add SSHResponse to SSHResponse")
        return SSHResponse(new_stdout, new_stderr)
