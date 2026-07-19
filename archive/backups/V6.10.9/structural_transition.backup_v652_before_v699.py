
class StructuralTransitionIntelligence:

    VERSION = "6.5.2"

    def analyze(self, signature, metrics):

        pressure = metrics.get(
            "evolution_pressure",
            0
        )

        density = signature.get(
            "density",
            0
        )

        if pressure > 5:
            state = "CRITICAL_TRANSITION"
        elif pressure > 2:
            state = "ACTIVE_TRANSITION"
        else:
            state = "STABLE_STRUCTURE"

        return {
            "version": self.VERSION,
            "state": state,
            "pressure": pressure,
            "density": density
        }
