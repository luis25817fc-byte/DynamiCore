
"""
DynamiCore V6.9.9
Dynamic Graph Intelligence Core
"""

from app.core.graph_intelligence.evolution_metrics import EvolutionMetrics
from app.core.graph_intelligence.structural_transition import StructuralTransitionIntelligence


class DynamicGraphIntelligence:

    VERSION = "6.5.1"


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

            "density": transition.get(
                "density",
                0
            ),

            "evolution_score": evolution_metrics.get(
                "evolution_pressure",
                0
            )

        }


        transition_intelligence = self.transition_engine.analyze(
            signature,
            evolution_metrics
        )


        return {

            "version": self.VERSION,

            "diff": diff,

            "transition": transition,

            "signature": signature,

            "evolution_metrics": evolution_metrics,

            "transition_intelligence": transition_intelligence,

            "decision": {},

            "intelligence": "ACTIVE"

        }
