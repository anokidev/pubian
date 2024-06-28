"""

    pubian.exceptions.logging

    Exceptions used by the Pubian Logging System
    (pubian.api_front.logging & pubian.core.api_back.logging),
    NOT including Pubian CLI Logging System (can be found in
    pubian.exceptions.cli)

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

class InvalidComponentRegisterType(Exception):
    """
        Used in pubian.api_front.logging.LoggingAPI.__init__
        when the app/addon types are not valid. The only available
        types are this: App / Frontware / Middleware / Backware.
        System is only allowed by Pubian itself.
    """

class InvalidLoggingLevel(Exception):
    """
        Used in pubian.core.api_back.log when the logging level
        is infalid. The only available levels are:
        - success
        - info
        - warning
        - error
        - critical
    """
