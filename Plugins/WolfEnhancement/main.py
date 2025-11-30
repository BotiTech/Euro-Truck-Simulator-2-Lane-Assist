from time import time
from ETS2LA.Utils import settings
from ETS2LA.Controls import *
from ETS2LA.Events import *
from ETS2LA.Plugin import *
from ETS2LA.UI import *

class Plugin(ETS2LAPlugin):
    description = PluginDescription(
        name="Wolf Enhancement",
        version="1.0.0",
        description="Base module of the Wolf Safety Enhancements plugin series.",
        modules=["SDKController"],
        fps_cap=20
    )

    author = [
        Author(
            name="Wuf",
            url="https://github.com/@BotiTech"
        )
    ]



    def init(self):
        self.controller = self.modules.SDKController.SCSController()
        print("Wolf Enhancement Plugin initialized.")
    
    def run(self):
        self.controller.horn = True
        time.sleep(1)
        self.controller.horn = False