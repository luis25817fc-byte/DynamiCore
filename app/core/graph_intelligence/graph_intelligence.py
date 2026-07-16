
"""
DynamiCore V6.11
Dynamic Graph Intelligence Evolution Core
"""

from app.core.graph_intelligence.evolution_metrics import EvolutionMetrics
from app.core.graph_intelligence.structural_transition import StructuralTransitionIntelligence


class DynamicGraphIntelligence:

    VERSION = "6.11.0"


    def __init__(self):

        self.metrics = EvolutionMetrics()

        self.transition_engine = StructuralTransitionIntelligence()



    def analyze(self, diff, transition):

        diff = diff or {}

        transition = transition or {}


        evolution_metrics = self.metrics.calculate(
            diff,
            transition
        )


        signature = {

            "density":
                transition.get(
                    "density",
                    0
                ),

            "evolution_score":
                evolution_metrics.get(
                    "evolution_pressure",
                    0
                ),

            "structural_variation":
                diff.get(
                    "structural_variation",
                    0
                ),

            "evolution_pressure":
                evolution_metrics.get(
                    "evolution_pressure",
                    0
                ),

            "transition_risk":
                transition.get(
                    "risk",
                    "UNKNOWN"
                )

        }


        transition_intelligence = self.transition_engine.analyze(
            signature,
            evolution_metrics
        )


        return {

            "version":
                self.VERSION,

            "diff":
                diff,

            "transition":
                transition,

            "signature":
                signature,

            "evolution_metrics":
                evolution_metrics,

            "transition_intelligence":
                transition_intelligence,

            "decision":
                {},

            "intelligence":
                "ACTIVE"

        }
