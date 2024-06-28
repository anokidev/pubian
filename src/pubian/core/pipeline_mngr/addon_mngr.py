"""

    pubian.core.pipeline_mngr.addon_mngr

    This contains the manager of application.
    - Obtaining the application configs.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

import os
import sys
import imp
import types
import importlib
from collections.abc import Callable

from pubian.core.logging import PubianCoreLogging

from pubian.exceptions.app import (
    AppIsNotActivated, 
    InvalidPubianApp, 
    MissingAppConf
)

class UsefulStuff(PubianCoreLogging):
    pass

class AddonManager(UsefulStuff):
    """Responsible for managing the application."""

    def __init__(self, name):
        self.app_log: Callable[[str, str], None] = PubianCoreLogging(
            "ADDON MANAGER").log

    def _get_addon_conf_and_main(self):
        """Get the application configuration."""

        # Check if the app is activated.
        