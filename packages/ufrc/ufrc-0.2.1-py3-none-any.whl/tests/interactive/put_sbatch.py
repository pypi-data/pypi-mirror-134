from settings import Settings, SETTINGS
from ufrc.main import UFRC
from ufrc.sbatch import SBatchHeaders, SBatchFile


def put_sbatch(settings: Settings):
    ufrc = UFRC()
    ufrc.connect(settings.username, settings.password)
    headers = SBatchHeaders(job_name="my_job", email="derobertisna@ufl.edu")
    sbatch = SBatchFile(commands=["module load python", "ls -l"], headers=headers)
    ufrc.put_sbatch(sbatch)


if __name__ == "__main__":
    put_sbatch(SETTINGS)
