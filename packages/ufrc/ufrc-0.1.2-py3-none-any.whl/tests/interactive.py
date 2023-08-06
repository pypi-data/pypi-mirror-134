from settings import Settings, SETTINGS
from ufrc.main import UFRC


def run_ls(settings: Settings):
    ufrc = UFRC()
    ufrc.connect(settings.username, settings.password)
    output = ufrc.run("ls")
    print(output)


if __name__ == "__main__":
    run_ls(SETTINGS)
