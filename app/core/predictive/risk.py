
class RiskEngine:

    def analyze(self, predictive, metrics):

        risk = 0

        if predictive["regime"] == "expanding":
            risk += 0.2

        if predictive["acceleration"] > 0:
            risk += 0.2

        if metrics["D(k)"]["anomaly"]:
            risk += 0.4

        if metrics["ΔR(k)"]["regime_change"]:
            risk += 0.2


        if risk >= 0.7:
            severity = "high"
            warning = True
        elif risk >= 0.4:
            severity = "medium"
            warning = True
        else:
            severity = "low"
            warning = False


        return {
            "risk_score": risk,
            "severity": severity,
            "warning": warning
        }
