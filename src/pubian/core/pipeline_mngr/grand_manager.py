"""

    pubian.core.pipeline_mngr.grand_manager

    This contains the grand manager, which
    is the manager of the pipeline. The pipeline
    itself is a process that manages the execution
    of each components (frontware, middleware, backware)
    in a controlled and timely manner. The pipeline also
    manages the file watcher, which utilizes watchdog as
    a way to watch for any changes.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

from pubian.core.pipeline_mngr import ProjectMngr
from pubian.core.pipeline_mngr import AppMngr
from pubian.core.pipeline_mngr import AddonMngr
from pubian.core.pipeline_mngr import FileWtchr

from pubian.core.logging import init_logging, PubianCoreLogging

from collections.abc import Callable

class GrandManager(ProjectMngr, AppMngr, AddonMngr, FileWtchr):
    """This is the grand manager class."""

    def __init__(self, cwd: str, app_name: str, default_conf: bool):
        self.cwd: str                            = cwd
        self.app_name: str                       = app_name
        self.default_conf: bool                  = default_conf
        self.grand_log: Callable[[str, str], None] = PubianCoreLogging(
            "GRAND MANAGER").log

    def __call__(self):
        """
            Here is the flow of the pipeline process:
            [01] Get the project configuration.
                > Note that the files have been checked by the CLI.
            [02] Get the addons list, debug mode, and application conf.
            [03] Configure the logging.
                > If DEBUG_MODE is true, logging will be reconfigured.
            [04] Extract the application configuration and main.
                > If default_conf is true, then don't extract the conf.
            [05] Get the configuration construct of every addons.
                > If default_conf is true, use the default value.
            [06] Compare the construct with the application configuration.
                > If default_conf is true, this process is skipped.
            [07] Get the file construct, and began following the construct.
            [08] Begin the file watcher.
                > If DEBUG_MODE is false, file watcher won't be initialized.
                > If there is an error, an exception handler will handle the error.
            [09] Begin executing the app, middleware, and backware.
                > This is the cycle.
            [10] If there is an error, the file watcher will be paused.
                > The components will be allowed to finish some stuff.
                > And then the process is halted, the exception is raised.
                > The file watcher will be waiting for any kind of changes.
                > If there is a change. The cycle will be turned on againn.
        """

        # From: ProjectMngr
        (
            self.DEBUG_MODE,
            self.ACTIVATED_APPS,
            self.FRONTWARE,
            self.MIDDLEWARE,
            self.BACKWARE
        ) = self._get_project_configs(self.__cwd) # 01, 02

        # From: This class.
        self.__configure_core_logging() # 03

        # From: AppMngr
        self._get_app_conf_and_main() # 04

        # From: AddonMngr
        self._get_addon_main() # 05

    def __configure_core_logging(self):
        """Configure CORE logging, not CLI logging."""

        # Set the logging level.
        init_logging(self._DEBUG_MODE) # The debug is from ProjectMngr
