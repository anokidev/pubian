"""

    pubian.api.addons

    The base class for an addon component.

"""

import logging

from pubian.exceptions.logging import LoggingExceptions

from pubian.core.logging import PubianCoreLogging

class UsefulStuff(PubianCoreLogging):
    pass

class PubianAddonClass(UsefulStuff):
    """Base class of an addon."""

    def __call__(self):
        """
            The steps:
            - Get the configuration.
            - 
        """

        (
            app_conf,       # Application configuration.
            define_config,  # A func that returns addon "config expectation".
            define_file,    # A func that returns addon "file expectation".
            my_task         # List of tasks related to the addon.
        )  = self.main()

        # Configuration construct is a dictionary containing
        # a hash of configs that the addon "expects".
        # From here the core can know what configs should be
        # picked up.
        config_construct: dict = define_config()

        # Same with configuration construct. But this time
        # it contains a dictionary that are full of files
        # that the addon "expects".
        file_construct: dict   = define_file()

      

    

    

        


