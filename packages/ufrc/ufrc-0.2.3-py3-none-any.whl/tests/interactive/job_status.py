from settings import Settings, SETTINGS
from ufrc.main import UFRC


def get_job_status(settings: Settings):
    ufrc = UFRC()
    ufrc.connect(settings.username, settings.password)
    status = ufrc.job_status(group_name=settings.group_name, user_id=settings.uid)
    print(status)


if __name__ == "__main__":
    get_job_status(SETTINGS)
