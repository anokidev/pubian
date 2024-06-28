"""

    pubian.core.pubian_cli

    Containing modules related to Pubian CLI.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

from pubian.core.pubian_cli.app import AppCommand
from pubian.core.pubian_cli.addon import AddonCommand
from pubian.core.pubian_cli.init import InitCommand

from pubian.core.pubian_cli.app_cmd.scaffold import AppScaffoldCommand
from pubian.core.pubian_cli.app_cmd.run import AppRunCommand
from pubian.core.pubian_cli.app_cmd.test import AppTestCommand

from pubian.core.pubian_cli.addon_cmd.scaffold import AddonScaffoldCommand
from pubian.core.pubian_cli.addon_cmd.run import AddonRunCommand
from pubian.core.pubian_cli.addon_cmd.test import AddonTestCommand

from pubian.core.pubian_cli.help import HELP

App:                    AppCommand
Addon:                  AddonCommand
Init:                   InitCommand

AppScaffold:            AppScaffoldCommand
AppRun:                 AppRunCommand
AppTest:                AppTestCommand

AddonScaffold:          AddonScaffoldCommand
AddonRun:               AddonRunCommand
AddonTest:              AddonTestCommand

HELP_COMMAND: str     = HELP

DEFAULT_TEMPLATE: str = "https://github.com/anokidev/pbtp-simple-test/archive/refs/heads/main.zip"

__all__ = [
    # These are managers for each commands.
    # Except HELP_COMMAND, which just prints out the
    # help message.
    App,
    Addon,
    Init,
    HELP_COMMAND,
    # pubian app [options]
    AppScaffold,
    AppRun,
    AppTest,
    # pubian addon [options]
    AddonScaffold,
    AddonRun,
    AddonTest,
    # Default template, used by pubian init
    DEFAULT_TEMPLATE
]
