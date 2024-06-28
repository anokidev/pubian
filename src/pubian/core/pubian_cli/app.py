"""

    pubian.core.pubian_cli.app

    For command: pubian app

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

import os
import sys

from pubian.core.pubian_cli import (AppScaffold, AppRun,
                                    AppTest, HELP_COMMAND)

from pubian.core.pipeline_mngr import GrandManager

from pubian.core.pubian_cli.log import log

class AppCommand(AppScaffold, AppRun, AppTest):
    """For command: pubian app"""
    
    def __init__(self, option: str, other: "list[str]", cwd: str):
        self.__option: str       = option
        self.__name: list[str]   = other[0]
        self.__flags: list[str]  = other[1:]
        self.__cwd: str          = cwd

    def __call__(self):
        """We begin by parsing the option and flags first :)"""

        # Parse the option.
        if self.__option == "scaffold":
            self.__scaffold()
        elif self.__option == "exec":
            self.__exec()
        elif self.__option == "run":
            self.__run()
        elif self.__option == "test":
            self.__test()
        else:
            print(HELP_COMMAND)
            sys.exit(1)

    def __scaffold(self) -> None:
        pass

    def __exec(self) -> None:
        """This function is for command: pubian app exec"""

        # Extract the flags.
        self.__default: bool = False

        # Check the flags.
        for i in self.__flags:
            if i == "--default":
                self.__default = True
            else:
                pass

        self.__check_project() # Check the project first.
        self.__run_project()   # Run the project.

    def __check_project(self) -> None:
        """Check if the project folder is a proper project folder or not."""

        log("Attemtping to extract project's config.py", "process")

        # First of all, config.py must exist.
        if os.path.exists(f"{self.__cwd}/config.py"):
            log("Success!", "success")
        else:
            log("Project config.py is not detected.", "failure")

        log("Attempting to detect apps and addons dir...", "process")

        # Second of all, apps and addons dir must exist.
        if os.path.exists(f"{self.__cwd}/apps/") and os.path.exists(f"{self.__cwd}/addons/"):
            log("Success!", "success")
        else:
            log("Both ./apps and ./addons are required.", "failure")

        # Third of all, the app itself must exist.
        if os.path.exists(f"{self.__cwd}/apps/{self.__name}"):
            log("Success!", "success")
        else:
            log(f"{self.__name} does not exist.", "failure")

        log("Attempting to extract app's config.py", "process")

        # Fourth of all, app's config.py must exist.
        if os.path.exists(f"{self.__cwd}/apps/{self.__name}/config.py"):
            log("Success!", "success")
        else:
            log("App config.py is not detected.", "failure")

    def __run_project(self):
        """Then, simply run the grand manager!"""

        log("Initiating grand manager and logging API...", "process")

        GrandManager(
            cwd=self.__cwd,
            app_name=self.__name,
            default_conf=self.__default
        )()

