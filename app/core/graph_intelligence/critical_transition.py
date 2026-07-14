
class CriticalTransitionDetector:

    VERSION = "7.0.0"

    def evaluate(self, predictive):

        predictive = predictive or {}

        probability = predictive.get(
            "transition_probability",
            0
        )

        risk = predictive.get(
            "risk_level",
            "LOW"
        )

        if probability >= 0.80:
            criticality = "HIGH"
            state = "CRITICAL_TRANSITION"

        elif probability >= 0.50:
            criticality = "MEDIUM"
            state = "ACTIVE_TRANSITION"

        else:
            criticality = "LOW"
            state = "STABLE_STRUCTURE"

        return {

            "version": self.VERSION,

            "criticality": criticality,

            "transition_state": state,

            "transition_probability": probability,

            "risk_level": risk

        }


# Compatibilidad V7
CriticalTransitionEngine = CriticalTransitionDetector
