"""

    pubian.exceptions.cli

    Exceptions used by the Pubian CLI
    (pubian.core.pubian_cli)

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

class InvalidCheckerReturnType(Exception):
    """
        An internal excep used if the checker
        (a function used by a function called
        pubian.core.pubian_cli.ask which is used
        to check the input of the user) returns
        a non-boolean value.
    """

class InvalidCLILoggingType(Exception):
    """
        An internal excep used if an invalid type
        is inserted into pubian.core.pubian_cli.log.log.

        For example:

        log("message", "xcv")

        Now there are only a few types that are available:
        - Success.
        - Info.
        - Warning.
        - Error.
        - Critical.

        There is no xcv, thus this error will be thrown.
    """