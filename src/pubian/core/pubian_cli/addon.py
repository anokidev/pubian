"""

    pubian.core.pubian_cli.app

    For command: pubian addon

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

import sys

from pubian.core.pubian_cli import (AddonScaffold, AddonRun,
                                    AddonTest, HELP_COMMAND)

class AddonCommand(AddonScaffold, AddonRun, AddonTest):
    """For command: pubian addon"""

    def __init__(self, option: str, flags: "list[str]", cwd: str):
        self.__option = option
        self.__flags  = flags
        self.__cwd    = cwd

    def __call__(self):
        """We begin by parsing the option and flags first :)"""

        # Parse the option.
        if self.__option == "scaffold":
            self.__scaffold()
        elif self.__option == "test":
            self.__test()
        else:
            print(HELP_COMMAND)
            sys.exit(1)
