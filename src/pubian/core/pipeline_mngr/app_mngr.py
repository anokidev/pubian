"""

    pubian.core.pipeline_mngr.app_mngr

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

class AppManager(UsefulStuff):
    """Responsible for managing the application."""

    def __init__(self, name):
        self.app_log: Callable[[str, str], None] = PubianCoreLogging(
            "APP MANAGER").log

    def _get_app_conf_and_main(self):
        """Get the application configuration."""

        # Check if the app is activated.
        if self.app_name not in self.activated_apps:
            raise AppIsNotActivated(f"{self.app_name} is not activated.")

        # Check if default_conf == True
        if self.default_conf:
            self.__extract_app_main_default()
        else:
            self.__extract_app_main_nondefault()

    def __extract_app_main_default(self):
        """Extract the application main.py only."""

        # If an app is marked with "*", the app is local.
        if self.app_name[0] == "*":
            if os.path.exists(
                f"{self.cwd}/apps/{self.app_name[1:]}/main.py") is not True:
                raise InvalidPubianApp(
                    f"{self.app_name} doesn't exist or its main.py is missing.")
            # Import the configuration.
            spec: types.ModuleSpec | None = importlib.util.spec_from_file_location(
                "app_config", f"{self.cwd}/apps/{self.app_name[1:]}/main.py")
            self._app_main: types.ModuleType = importlib.util.module_from_spec(spec)
            sys.modules["app_config"] = self._app_main
            spec.loader.exec_module(self._app_main)
            # Set the app conf to None (default conf)
            self._app_conf = None
        else:
            try:
                imp.find_module(f"{self.app_name}.main")
            except ImportError:
                raise InvalidPubianApp(
                    f"{self.app_name} is not installed or its main.py is missing.")
            self._app_main: types.ModuleType = importlib.import_module(
                f"{self.app_name}.main")
            # Set the app conf to None (default conf)
            self._app_conf = None

    def __extract_app_main_nondefault(self):
        """Extract the application main.py and configuration."""

        # If an app is marked with "*", the app is local.
        if self.app_name[0] == "*":
            if os.path.exists(
                f"{self.cwd}/apps/{self.app_name[1:]}/main.py") is not True:
                raise InvalidPubianApp(
                    f"{self.app_name} doesn't exist or its main.py is missing.")
            # Import the configuration.
            spec: types.ModuleSpec | None = importlib.util.spec_from_file_location(
                "app_config", f"{self.cwd}/apps/{self.app_name[1:]}/main.py")
            self._app_main: types.ModuleType = importlib.util.module_from_spec(spec)
            sys.modules["app_config"] = self._app_main
            spec.loader.exec_module(self._app_main)
            # Get the app_conf
            try:
                self._app_conf: types.ModuleType = self._app_main.Main.app_conf
            except AttributeError:
                raise MissingAppConf("Unable to import app_conf. If you don't want to use default conf, please provide flag \"--default-conf\".")
        # If not, the app is installed.
        else:
            try:
                imp.find_module(f"{self.app_name}.main")
            except ImportError:
                raise InvalidPubianApp(
                    f"{self.app_name} is not installed or its main.py is missing.")
            self._app_main: types.ModuleType = importlib.import_module(
                f"{self.app_name}.main")
            # Get the app_conf
            try:
                self._app_conf: types.ModuleType = self._app_main.Main.app_conf
            except AttributeError:
                raise MissingAppConf("Unable to import app_conf. If you don't want to use default conf, please provide flag \"--default-conf\".")
