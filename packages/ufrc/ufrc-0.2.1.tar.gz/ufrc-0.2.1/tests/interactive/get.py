from settings import Settings, SETTINGS
from ufrc.main import UFRC


def get_file(settings: Settings):
    ufrc = UFRC()
    ufrc.connect(settings.username, settings.password)
    ufrc.get("temp.txt")


if __name__ == "__main__":
    get_file(SETTINGS)
