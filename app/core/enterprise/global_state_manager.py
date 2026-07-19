
class EnterpriseGlobalStateManager:

    VERSION = "6.7.8"


    def __init__(self):

        self.state = {
            "system": "DynamiCore",
            "status": "INITIALIZED"
        }


    def update(
        self,
        component,
        data
    ):

        self.state[component] = data

        return {

            "version":
                self.VERSION,

            "updated":
                True,

            "component":
                component
        }


    def snapshot(self):

        return {

            "version":
                self.VERSION,

            "global_state":
                self.state,

            "status":
                "ACTIVE"
        }
