from . import config as app_config

from pubian.api.apps import PubianAppClass

class Main(PubianAppClass):

    app_config

    def main(self):
        return (
            self.define_config,
            self.define_file,
            [self.my_task]
        )
