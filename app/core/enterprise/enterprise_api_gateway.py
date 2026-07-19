
class EnterpriseAPIGateway:

    VERSION = "6.8.2"

    def __init__(
        self,
        gateway
    ):

        self.gateway = gateway


    def execute(
        self,
        previous,
        current,
        source="API"
    ):

        response = self.gateway.request(
            previous,
            current,
            source
        )

        return {

            "version":
                self.VERSION,

            "status":
                "SUCCESS",

            "response":
                response
        }
