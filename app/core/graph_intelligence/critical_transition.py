
class CriticalTransitionDetector:

    VERSION = "6.5.5"

    def analyze(
        self,
        evolution_metrics,
        predictive_structural,
        transition_intelligence
    ):

        pressure = evolution_metrics.get(
            "evolution_pressure",
            0
        )

        probability = predictive_structural.get(
            "transition_probability",
            0
        )

        state = transition_intelligence.get(
            "state",
            "UNKNOWN"
        )

        if pressure >= 7 or probability >= 0.7:
            criticality = "HIGH"
            crossed = True
            transition_state = "CRITICAL"

        elif pressure >= 4 or probability >= 0.4:
            criticality = "MEDIUM"
            crossed = True
            transition_state = "EMERGING"

        else:
            criticality = "LOW"
            crossed = False
            transition_state = state

        return {
            "version": self.VERSION,
            "transition_state": transition_state,
            "criticality": criticality,
            "threshold_crossed": crossed,
            "warning": (
                "STRUCTURAL_REGIME_CHANGE"
                if crossed
                else "NO_CRITICAL_TRANSITION"
            )
        }
