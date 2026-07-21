
"""
DynamiCore DLIS-002

Structural Pressure Engine

Pi = ΔH + ΔD + (1-R)

"""


class StructuralPressureEngine:

    VERSION = "DLIS-002"


    def compute(
        self,
        entropy_change,
        divergence_change,
        resilience
    ):

        pressure = (
            entropy_change +
            divergence_change +
            (1 - resilience)
        )


        return {

            "version": self.VERSION,

            "delta_entropy":
                entropy_change,

            "delta_divergence":
                divergence_change,

            "resilience":
                resilience,

            "pressure":
                pressure

        }
