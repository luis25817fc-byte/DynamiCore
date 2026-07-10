
from .graph import CausalGraph



class CausalEngine:


    def __init__(self):

        self.graph = CausalGraph()



        # Relaciones iniciales del sistema

        self.graph.add_relation(
            "coherence_drop",
            "system_instability",
            0.8
        )


        self.graph.add_relation(
            "divergence_growth",
            "risk_increase",
            0.7
        )


        self.graph.add_relation(
            "entropy_growth",
            "complexity_increase",
            0.6
        )



    def analyze(
        self,
        attribution
    ):


        dominant = attribution[
            "dominant_factor"
        ]


        effects = self.graph.get_effects(
            dominant
        )


        confidence = attribution[
            "confidence"
        ]



        return {


            "cause":

                dominant,


            "effects":

                effects,


            "confidence":

                confidence,


            "causal_found":

                len(effects) > 0

        }
