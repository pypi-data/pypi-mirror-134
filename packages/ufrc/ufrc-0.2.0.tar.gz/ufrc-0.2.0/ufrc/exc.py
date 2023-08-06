class UFRCException(Exception):
    pass


class UFRCSSHException(UFRCException):
    pass


class NoUFRCConnectionException(UFRCSSHException):
    pass
