from enum import Enum
from typing import List, Union, Optional

from pydantic import BaseModel, Field


class MailType(str, Enum):
    NONE = "NONE"
    BEGIN = "BEGIN"
    END = "END"
    FAIL = "FAIL"
    ALL = "ALL"


class SBatchHeaders(BaseModel):
    job_name: str
    email: str
    memory_mb: int = 1000
    n_tasks: int = 1
    cpus_per_task: int = 1
    mail_types: List[MailType] = Field(
        default_factory=lambda: [MailType.END, MailType.FAIL]
    )
    output: str = "%j.log"
    time: str = "14-0:00"
    array: Optional[str] = None

    @property
    def header_str(self) -> str:
        headers = [
            _sbatch_line("job-name", self.job_name),
            _sbatch_line("mail-user", self.email),
            _sbatch_line("mem", f"{self.memory_mb}mb"),
            _sbatch_line("ntasks", self.n_tasks),
            _sbatch_line("cpus-per-task", self.cpus_per_task),
            _sbatch_line("mail-type", self.mail_types),  # type: ignore
            _sbatch_line("time", self.time),
            _sbatch_line("output", self.output),
        ]
        if self.array is not None:
            headers.append(_sbatch_line("array", self.array))
        return "\n".join(headers)


SBatchPrimitive = Union[str, int, MailType]
SBatchValue = Union[SBatchPrimitive, List[SBatchPrimitive]]


def _sbatch_line(flag_name: str, value: SBatchValue) -> str:
    return f"#SBATCH --{flag_name}={_to_sbatch_value_str(value)}"


def _to_sbatch_value_str(value: SBatchValue) -> str:
    if isinstance(value, list):
        return ",".join(_sbatch_primitive_to_str(v) for v in value)
    return _sbatch_primitive_to_str(value)


def _sbatch_primitive_to_str(value: SBatchPrimitive) -> str:
    if isinstance(value, Enum):
        return str(value.value)
    return str(value)


class SBatchFile(BaseModel):
    commands: List[str]
    headers: SBatchHeaders
    shebang: str = "#!/bin/bash"

    @property
    def contents(self) -> str:
        outputs = [self.shebang, self.headers.header_str, *self.commands]
        return "\n".join(outputs)
