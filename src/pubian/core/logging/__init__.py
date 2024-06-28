"""

    pubian.core.logging

    Containing the inner workings of logging.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

from .tools import init_logging, PubianAddonLogging, PubianAppLogging, PubianCoreLogging

init_logging      = init_logging
PubianCoreLogging = PubianCoreLogging

__all__ = [PubianAddonLogging, PubianAppLogging]
