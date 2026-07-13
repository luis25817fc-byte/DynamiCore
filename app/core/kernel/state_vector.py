
# ==============================================================
# DynamiCore V6.9.8
# Unified State Vector Contract
# ==============================================================


class StateVector:

    VERSION = "6.9.8"


    def __init__(
        self,
        entropy=0.0,
        coherence=0.0,
        delta=0.0,
        potential=0.0,
        divergence=0.0,
        dynamics=0.0,
        **kwargs
    ):

        self.entropy = entropy

        self.coherence = coherence

        self.delta = delta

        self.potential = potential

        self.divergence = divergence

        self.dynamics = dynamics


        # compatibility fields

        for key, value in kwargs.items():

            setattr(
                self,
                key,
                value
            )


    def to_dict(self):

        return {

            "version":
                self.VERSION,

            "entropy":
                self.entropy,

            "coherence":
                self.coherence,

            "delta":
                self.delta,

            "potential":
                self.potential,

            "divergence":
                self.divergence,

            "dynamics":
                self.dynamics
        }


    def __repr__(self):

        return str(
            self.to_dict()
        )
