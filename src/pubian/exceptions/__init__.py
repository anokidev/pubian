"""

    pubian.exceptions

    Exceptions used by Pubian. Here are
    the terminologies:
    - Internal Excep: Only used by Pubian,
    not the apps nor the addons.
    - External Excep: Used by Pubian, apps,
    and the addons.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

from pubian.exceptions.logging import InvalidComponentRegisterType, InvalidLoggingLevel

class LoggingExceptions:
    """
        A collection of core logging exceptions, used by:
        - pubian.api_front.logging
        - pubian.core.api_back.logging
    """

    InvalidComponentRegisterType = InvalidComponentRegisterType
    InvalidLoggingLevel = InvalidLoggingLevel

__all__ = [
    LoggingExceptions
]
