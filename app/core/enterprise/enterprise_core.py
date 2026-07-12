
class EnterpriseCore:

    VERSION = "6.7.0"

    def __init__(
        self,
        orchestrator,
        security,
        config,
        deployment
    ):

        self.orchestrator = orchestrator
        self.security = security
        self.config = config
        self.deployment = deployment


    def start(
        self,
        token,
        state
    ):

        security = self.security.authenticate(
            token
        )

        if not security["authenticated"]:

            return {
                "version": self.VERSION,
                "status": "SECURITY_BLOCKED"
            }


        result = self.orchestrator.execute(
            state
        )


        return {

            "version": self.VERSION,

            "status":
                "ENTERPRISE_ACTIVE",

            "security":
                security,

            "system":
                result,

            "configuration":
                self.config.get(),

            "deployment":
                self.deployment.audit()
        }
