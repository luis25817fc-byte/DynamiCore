
"""
DynamiCore DLIS-001

Structural Potential Engine

Psi(S)=H(S)*D(S)/(R(S)+epsilon)

"""


class StructuralPotentialEngine:

    VERSION = "DLIS-001"


    def __init__(self, epsilon=1e-9):

        self.epsilon = epsilon


    def compute(
        self,
        entropy,
        divergence,
        resilience
    ):

        potential = (
            entropy *
            divergence
        ) / (
            resilience +
            self.epsilon
        )


        return {

            "version": self.VERSION,

            "entropy": entropy,

            "divergence": divergence,

            "resilience": resilience,

            "potential": potential

        }
