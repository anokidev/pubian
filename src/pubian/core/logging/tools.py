"""

    pubian.core.logging.class

    Containing classes to be extended by addons and apps.
    Each class contains logging methods. This file also
    contains init_logging, which is used to configure
    the logging module.

"""

import logging

from pubian.exceptions.logging import LoggingExceptions

def init_logging(debug: bool) -> None:
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

class PubianAddonLogging:
    """This one will be used by PubianAddonClass"""

    def log(self, message: str, level: str) -> None:
        """
            Log a message. 
            - name: addon name.
            - type: [frontware / middleware / backware]
        """

        output: str = f"[{level}] [{self.__type}] [{self.__name}] {message}"
        if level == "success":
            logging.info(output)
        elif level == "info":
            logging.info(output)
        elif level == "warning":
            logging.warning(output)
        elif level == "error":
            logging.error(output)
        elif level == "critical":
            logging.critical(output)
        else:
            raise LoggingExceptions.InvalidLoggingLevel(
                f"Invalid logging level: {level}")
        
class PubianAppLogging:
    """This one will be used by PubianAppClass"""

    def log(self, message: str, level: str) -> None:
        """
            Log a message. 
            - name: app name.
        """

        output: str = f"[{level}] [APP] [{self.__name}] {message}"
        if level == "success":
            logging.info(output)
        elif level == "info":
            logging.info(output)
        elif level == "warning":
            logging.warning(output)
        elif level == "error":
            logging.error(output)
        elif level == "critical":
            logging.critical(output)
        else:
            raise LoggingExceptions.InvalidLoggingLevel(
                f"Invalid logging level: {level}")
        
class PubianCoreLogging:
    """This one will be used by PubianCoreClass"""

    def __init__(self, name: str):
        self.__name = name

    def log(self, message: str, level: str) -> None:
        """
            Log a message. 
            - name: core component name.
        """

        output: str = f"[{level}] [CORE] [{self.__name}] {message}"
        if level == "success":
            logging.info(output)
        elif level == "info":
            logging.info(output)
        elif level == "warning":
            logging.warning(output)
        elif level == "error":
            logging.error(output)
        elif level == "critical":
            logging.critical(output)
        else:
            raise LoggingExceptions.InvalidLoggingLevel(
                f"Invalid logging level: {level}")
