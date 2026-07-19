
"""
DynamiCore V6.11.1
Graph Intelligence Enterprise Pipeline
"""


from .graph_delta import GraphDeltaEngine
from .structural_signature import StructuralSignatureEngine
from .structural_signature_v2 import StructuralSignatureV2
from .evolution_layer import EvolutionLayer
from .evolution_metrics import EvolutionMetrics
from .predictive_structural import PredictiveStructuralLayer
from .critical_transition import CriticalTransitionDetector
from .dynamic_intelligence_state import DynamicIntelligenceState
from .structural_transition import StructuralTransitionIntelligence
from .structural_fusion import StructuralIntelligenceFusion
from .decision_engine import DecisionEngine



class GraphIntelligencePipeline:


    VERSION = "6.11.1"



    def __init__(self):

        self.delta = GraphDeltaEngine()

        self.signature = StructuralSignatureEngine()

        self.signature_v2 = StructuralSignatureV2()

        self.evolution = EvolutionLayer()

        self.metrics = EvolutionMetrics()

        self.predictive = PredictiveStructuralLayer()

        self.critical = CriticalTransitionDetector()

        self.transition = StructuralTransitionIntelligence()

        self.fusion = StructuralIntelligenceFusion()

        self.dynamic_state = DynamicIntelligenceState()

        self.decision = DecisionEngine()



    def run(
        self,
        previous,
        current
    ):


        previous = previous or {}

        current = current or {}



        previous_signature = self.signature.generate(
            previous
        )


        current_signature = self.signature.generate(
            current
        )



        signature_evolution = self.signature_v2.compare(
            previous_signature,
            current_signature
        )



        delta = self.delta.compare(
            previous,
            current
        )



        evolution = self.evolution.analyze(
            previous_signature,
            current_signature
        )



        metrics = self.metrics.calculate(
            delta,
            evolution
        )



        critical_metrics = {

            **metrics,

            **evolution,

            "evolution_pressure":
                evolution.get(
                    "structural_pressure",
                    evolution.get(
                        "evolution_score",
                        0
                    )
                )

        }



        transition = self.transition.analyze(
            current_signature,
            metrics
        )



        prediction = self.predictive.predict(
            critical_metrics
        )



        critical = self.critical.analyze(
            critical_metrics,
            prediction,
            transition
        )



        decision = self.decision.analyze(
            current_signature,
            evolution,
            prediction
        )



        state = self.dynamic_state.build(
            current_signature,
            prediction,
            critical,
            decision
        )



        return {


            "version":
                self.VERSION,


            "status":
                "GRAPH_INTELLIGENCE_PIPELINE_ACTIVE",


            "signature":
                current_signature,


            "signature_evolution":
                signature_evolution,


            "delta":
                delta,


            "evolution":
                evolution,


            "metrics":
                metrics,


            "transition":
                transition,


            "prediction":
                prediction,


            "critical_transition":
                critical,


            "dynamic_state":
                state,


            "decision":
                decision

        }
