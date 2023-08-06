from ufrc.sbatch import SBatchHeaders, SBatchFile

EXPECT_SBATCH_HEADERS = """
#SBATCH --job-name=my_job
#SBATCH --mail-user=derobertisna@ufl.edu
#SBATCH --mem=1000mb
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END,FAIL
#SBATCH --time=14-0:00
#SBATCH --output=%j.log
""".strip()

EXPECT_SBATCH_FILE = f"""
#!/bin/bash
{EXPECT_SBATCH_HEADERS}
module load python
ls -l
""".strip()


def test_sbatch_headers():
    sbatch = SBatchHeaders(job_name="my_job", email="derobertisna@ufl.edu")
    output = sbatch.header_str
    assert output == EXPECT_SBATCH_HEADERS


def test_sbatch_headers_with_array():
    sbatch = SBatchHeaders(job_name="my_job", email="derobertisna@ufl.edu", array="1-5")
    output = sbatch.header_str
    assert output == EXPECT_SBATCH_HEADERS + "\n#SBATCH --array=1-5"


def test_sbatch_file():
    headers = SBatchHeaders(job_name="my_job", email="derobertisna@ufl.edu")
    sbatch = SBatchFile(commands=["module load python", "ls -l"], headers=headers)
    output = sbatch.contents
    assert output == EXPECT_SBATCH_FILE
