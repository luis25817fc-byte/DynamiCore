
from datetime import datetime


class RuntimeRegistry:

    VERSION = "7.1"

    def __init__(self):
        self.modules = {}
        self.created = datetime.utcnow()


    def register(self, name, component):
        self.modules[name] = {
            "component": component.__class__.__name__,
            "status": "ACTIVE",
            "registered": datetime.utcnow()
        }


    def health(self):

        return {
            "version": self.VERSION,
            "timestamp": datetime.utcnow(),
            "modules": {
                k: {
                    "component": v["component"],
                    "status": v["status"]
                }
                for k,v in self.modules.items()
            },
            "status": "ONLINE"
        }


    def get(self, name):

        return self.modules.get(name)
