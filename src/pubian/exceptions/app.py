"""

    pubian.exceptions.app

    This contains the manager of application.
    - Obtaining the application configs.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

class AppIsNotActivated(Exception):
    """
        Used in pubian.pipeline_mngr.app_mngr
        if the app is not in the list of activated apps.
    """

class InvalidPubianApp(Exception):
    """
        Used in pubian.pipeline
    """

class 
