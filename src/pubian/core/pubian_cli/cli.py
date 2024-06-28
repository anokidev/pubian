"""

    pubian.core.pubian_cli.cli

    Entry-point to the CLI.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

import os
import sys

from pubian.core.pubian_cli import App, Addon, Init, HELP_COMMAND

def run_pubian_cli() -> None:
    """Run the Pubian CLI."""

    cwd: str        = os.getcwd()
    argv: list[str] = sys.argv

    # Command.
    try:
        command = argv[1]
    except IndexError:
        command = None
    
    # Option.
    try:
        option = argv[2]
    except IndexError:
        option = None

    # Flags.
    try:
        other = argv[2:]
    except IndexError:
        other = []

    # Test the command.
    if command == "init":
        Init(option, other, cwd)()
    elif command == "app":
        App(option, other, cwd)()
    elif command == "addon":
        Addon(option, other, cwd)()
    elif command in ("help", "--help", "-h"):
        print(HELP_COMMAND)
        sys.exit(0)
    else:
        print(HELP_COMMAND)
        sys.exit(1)
        