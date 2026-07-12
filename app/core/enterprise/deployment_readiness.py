
class DeploymentReadiness:

    VERSION = "6.6.9"

    def __init__(
        self,
        components=None
    ):

        self.components = components or {}


    def audit(self):

        checks = {}

        for name, status in self.components.items():
            checks[name] = bool(status)


        ready = all(
            checks.values()
        ) if checks else False


        return {

            "version": self.VERSION,

            "deployment":
                "READY"
                if ready
                else "PENDING",

            "checks":
                checks,

            "readiness_score":
                (
                    sum(checks.values())
                    /
                    len(checks)
                )
                if checks
                else 0
        }
