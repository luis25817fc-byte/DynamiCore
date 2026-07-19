
from datetime import datetime


class IntelligenceKernel:

    VERSION = "7.1"

    def __init__(self):

        self.created = datetime.utcnow()

        self.modules = {
            "graph_intelligence": False,
            "prediction": False,
            "decision": False,
            "enterprise": False
        }


    def register(self, name):

        if name in self.modules:
            self.modules[name] = True


    def status(self):

        return {
            "version": self.VERSION,
            "created": self.created,
            "modules": self.modules,
            "status": "ONLINE"
        }


    def health(self):

        active = sum(
            1 for x in self.modules.values()
            if x
        )

        return {
            "active_modules": active,
            "total_modules": len(self.modules),
            "health": active / len(self.modules),
            "status": "ONLINE"
        }
