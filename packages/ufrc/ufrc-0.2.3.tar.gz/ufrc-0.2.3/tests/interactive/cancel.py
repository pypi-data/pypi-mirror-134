from settings import Settings, SETTINGS
from ufrc.main import UFRC


def cancel_job(settings: Settings):
    ufrc = UFRC()
    ufrc.connect(settings.username, settings.password)
    result = ufrc.cancel_jobs_by_lookup(
        group_name=settings.group_name,
        user_id=settings.uid,
        job_name="capiq-web-crawler",
    )
    print(result)


if __name__ == "__main__":
    cancel_job(SETTINGS)
