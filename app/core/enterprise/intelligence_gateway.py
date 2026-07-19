
class EnterpriseIntelligenceGateway:

    VERSION = "6.8.1"


    def __init__(
        self,
        intelligence_core
    ):

        self.core = intelligence_core


    def request(
        self,
        previous,
        current,
        source="external"
    ):

        result = self.core.analyze(
            previous,
            current
        )

        return {

            "version":
                self.VERSION,

            "gateway_status":
                "ACTIVE",

            "source":
                source,

            "intelligence_result":
                result
        }
