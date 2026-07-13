

class StateVector:

    VERSION = "6.9.8"


    def __init__(
        self,
        entropy=0.0,
        coherence=0.0,
        delta=0.0,
        potential=0.0,
        divergence=0.0,
        dynamics=0.0
    ):

        self.entropy = entropy

        self.coherence = coherence

        self.delta = delta

        self.potential = potential

        self.divergence = divergence

        self.dynamics = dynamics



    def to_dict(self):

        return {

            "entropy": self.entropy,

            "coherence": self.coherence,

            "delta": self.delta,

            "potential": self.potential,

            "divergence": self.divergence,

            "dynamics": self.dynamics

        }



    @classmethod
    def from_dict(cls,data):

        return cls(

            entropy=data.get(
                "entropy",
                0
            ),

            coherence=data.get(
                "coherence",
                0
            ),

            delta=data.get(
                "delta",
                0
            ),

            potential=data.get(
                "potential",
                0
            ),

            divergence=data.get(
                "divergence",
                0
            ),

            dynamics=data.get(
                "dynamics",
                data.get(
                    "delta",
                    0
                )
            )

        )

