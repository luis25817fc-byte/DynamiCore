
"""
DynamiCore V6.10.9
Predictive Structural Intelligence
"""


class PredictiveStructuralLayer:

    VERSION = "6.10.9"


    def _clamp(self, value):

        return max(
            0,
            min(
                1,
                value
            )
        )


    def predict(
        self,
        fusion,
        history=None
    ):

        fusion = fusion or {}

        evolution_pressure = float(
            fusion.get(
                "evolution_pressure",
                0
            )
        )

        density = float(
            fusion.get(
                "density",
                0
            )
        )

        stability = float(
            fusion.get(
                "stability",
                1
            )
        )

        divergence = float(
            fusion.get(
                "divergence",
                0
            )
        )

        system_state = fusion.get(
            "system_state",
            "UNKNOWN"
        )


        pressure_score = self._clamp(
            evolution_pressure / 10
        )


        transition_probability = self._clamp(
            (
                pressure_score
                +
                divergence
                +
                (1 - stability)
            )
            /
            3
        )


        if transition_probability >= 0.80:

            future_state = "CRITICAL"
            risk = "HIGH"
            warning = True


        elif transition_probability >= 0.50:

            future_state = "PRE_CRITICAL"
            risk = "MEDIUM"
            warning = True


        elif transition_probability >= 0.25:

            future_state = "EVOLVING"
            risk = "LOW"
            warning = False


        else:

            future_state = system_state
            risk = "LOW"
            warning = False



        confidence = self._clamp(
            (
                stability
                +
                (1 - divergence)
            )
            /
            2
        )


        return {

            "version":
                self.VERSION,

            "current_state":
                system_state,

            "future_state":
                future_state,

            "risk_level":
                risk,

            "transition_probability":
                round(
                    transition_probability,
                    4
                ),

            "structural_pressure":
                round(
                    pressure_score,
                    4
                ),

            "early_warning":
                warning,

            "confidence":
                round(
                    confidence,
                    4
                )
        }
