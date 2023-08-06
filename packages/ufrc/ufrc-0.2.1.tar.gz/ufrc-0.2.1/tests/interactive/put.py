from settings import Settings, SETTINGS
from ufrc.main import UFRC


def put_file(settings: Settings):
    ufrc = UFRC()
    ufrc.connect(settings.username, settings.password)
    ufrc.put("codecov.yml")


if __name__ == "__main__":
    put_file(SETTINGS)
