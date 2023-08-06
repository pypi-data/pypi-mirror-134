import pytest

from ufrc.exc import NoUFRCConnectionException
from ufrc.main import UFRC

# TODO: add automated tests by mocking UFRC SSH session


def test_cannot_run_when_not_connected():
    rc = UFRC()
    with pytest.raises(NoUFRCConnectionException):
        rc.run("ls")
