
"""
DynamiCore DLIS-004

Evolution Balance Engine

dPsi/dt = Pi - Omega

"""


class EvolutionBalanceEngine:

    VERSION = "DLIS-004"


    def compute(
        self,
        pressure,
        coherence
    ):

        delta_psi = (
            pressure -
            coherence
        )


        if delta_psi > 0:
            regime = "TRANSITION"

        elif delta_psi < 0:
            regime = "STABLE"

        else:
            regime = "EQUILIBRIUM"


        return {

            "version":
                self.VERSION,

            "pressure":
                pressure,

            "coherence":
                coherence,

            "delta_psi":
                delta_psi,

            "regime":
                regime

        }
