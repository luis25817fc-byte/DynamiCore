
class AuthorityWiring:

    VERSION = "DLIS-047"


    def __init__(
        self,
        authority,
        components=None
    ):

        self.authority = authority
        self.components = components or {}



    def connect(self):

        self.authority.kernel = (
            self.components.get("kernel")
        )

        self.authority.runtime = (
            self.components.get("runtime")
        )

        self.authority.governance = (
            self.components.get("governance")
        )

        self.authority.validation = (
            self.components.get("validation")
        )

        self.authority.rollback = (
            self.components.get("rollback")
        )

        self.authority.observation = (
            self.components.get("observation")
        )

        self.authority.event_bus = (
            self.components.get("event_bus")
        )


        return {

            "version":
                self.VERSION,

            "status":
                "WIRED",

            "connected":
                [
                    name
                    for name, value
                    in self.components.items()
                    if value is not None
                ]

        }



    def status(self):

        return {

            "version":
                self.VERSION,

            "module":
                "AuthorityWiring",

            "status":
                "ONLINE"

        }
