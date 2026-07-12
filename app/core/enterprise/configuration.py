
class EnterpriseConfiguration:

    VERSION = "6.6.8"

    def __init__(self):

        self.config = {
            "environment": "production",
            "runtime_mode": "enterprise",
            "monitoring": True,
            "security": True,
            "persistence": True
        }


    def get(self):

        return {
            "version": self.VERSION,
            "configuration": self.config
        }


    def update(
        self,
        key,
        value
    ):

        self.config[key] = value

        return {
            "version": self.VERSION,
            "updated": True,
            "key": key,
            "value": value
        }
