"""

    pubian.core.pubian_cli.init

    For command: pubian init

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

import io
import os
import zipfile
from urllib.request import urlopen

from pubian.core.pubian_cli import DEFAULT_TEMPLATE
from pubian.core.pubian_cli.log import ask, confirm, log

class InitCommand:
    """For command: pubian init"""

    def __init__(self, option: str, flags: "list[str]", cwd: str):
        self.__name: str        = option
        self.__flags: list[str] = flags
        self.__cwd: str         = cwd

    def __call__(self):
        """We begin by parsing the info, then finish by initializing the project."""

        log("Collecting information...", "process")

        # Ask about the project name.
        if (self.__name == None):
            message: str = "Enter the project name, no whitespace."
            self.__name: str = ask(message, self.name_requirements)
        else:
            pass

        # Template variable.
        self.__template: str = None

        # Check the flags if the flags contain templates.
        for i in self.__flags:
            if i.startswith("--template"):
                    self.__template = i.lstrip("=")[1:]
                    if self.__template == "":
                        log("Invalid template.", "failure")
                    break
            
        # Interactive message for templates.
        if (self.__template is None):
            result: bool = confirm("Do you wish to use a custom template?")
            if result:
                message: str = "Enter the template URL."
                self.__template: str = ask(message, self.template_requirements)
            else:
                self.__template: str = DEFAULT_TEMPLATE

        log("Initializing project...", "process")

        # Initialize project.
        self.__initialize_project()

        log("Finished.", "success")

    def __initialize_project(self):
        """Get the archive zip, extract it on the folder."""

        try:
            # Obtained response.
            response = urlopen(self.__template)
            # Get the folder.
            with zipfile.ZipFile(io.BytesIO(response.read())) as archive:
                archive.extractall(f'{self.__cwd}')
                os.rename(
                    f"{self.__cwd}/{archive.namelist()[0]}",
                    f"{self.__cwd}/{self.__name}"
                )
                archive.close()
        except Exception as e:
            log("Failed to obtain template file.", "failure")
            raise e

    def name_requirements(self, response: str) -> bool:
        """Checking the project name."""

        value: bool = True

        for i in response:
            if i.isspace():
                value = False
                break
            else:
                value = True
                continue

        return value
    
    def template_requirements(self, response: str) -> bool:
        """Checking the template URL."""

        if response.startswith("http"):
            return True
        else:
            return False


