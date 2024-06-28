"""

    pubian.core.pubian_cli.log

    Logging utils for Pubian CLI only.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

import sys

from pubian.exceptions.cli import InvalidCLILoggingType, InvalidCheckerReturnType

def ask(message: str, func: callable) -> str:
    """A CLI logging tool to ask a question for an interactive setup."""

    print(f"> {message}")
    response: str = input(": ")
    result: bool  = func(response)

    if result is not bool:
        raise InvalidCheckerReturnType(f"{func.__name__} does not return a boolean value.")

    if result:
        return response
    else:
        return ask(message, func)
    
def confirm(message: str) -> bool:
    """A CLI logging tool to confirm with true or false."""

    print(f"> {message} [Y/N]")
    response: str = input(": ")
    
    if response in ("y", "Y"):
        return True
    elif response in ("n", "N"):
        return False
    else:
        return confirm(message)

def log(message: str, level: str) -> None:
    """Log a message to the console."""
    
    if level == "success":    
        print(f"[SUCCESS] {message}")
    elif level == "warn":
        print(f"[WARNING] {message}")
    elif level == "process":
        print(f"[PROCESS] {message}")
    elif level == "error":
        print(f"[ERROR] {message}")
    elif level == "failure":
        print(f"[FAILED] {message}")
        sys.exit(1)
    else:
        raise InvalidCLILoggingType(
            "{level} is not within the available CLI logging types."
        )