from . import config as addon_config

from pubian.api.addons import PubianAddonClass

class Main(PubianAddonClass):

    addon_config

    def main(self):
        return (
            self.define_config,
            self.define_file,
            [self.my_task]
        )

    def define_config(self):
        return {
            "HOST" : (str, "0.0.0.0"),
            "PORT" : (int, 8000),
            "SOME_DATA" : {
                "a" : (str, "Abc"),
                "b" : ([str, str], None),
                "c" : (tuple(int), ()),
                "d" : ((int, int), ()),
                "e" : (dict, {
                    "x" : str,
                    "y" : int,
                    "z" : float
                })
            }
        }
    
    def define_file(self):
        return {
            "a.py" : ["abc", "xyz"],
            "b.fd" : {
                "x.py" : ["run_conf", "test"]
            }
        }
    
    def my_task(self):
        pass
