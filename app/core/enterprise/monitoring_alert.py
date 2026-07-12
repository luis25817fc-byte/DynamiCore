
class EnterpriseMonitoringAlert:

    VERSION = "6.6.4"

    def analyze(
        self,
        state
    ):

        risk = state.get(
            "risk",
            "UNKNOWN"
        )

        if risk == "HIGH":
            alert = "CRITICAL_ALERT"

        elif risk == "MEDIUM":
            alert = "WARNING_ALERT"

        else:
            alert = "NO_ALERT"


        return {
            "version": self.VERSION,
            "monitoring": "ACTIVE",
            "risk": risk,
            "alert": alert,
            "source": "enterprise_monitor"
        }
