
from app.core.graph_intelligence.evolution_predictor import GraphEvolutionPredictor
from app.core.graph_intelligence.predictive_structural import PredictiveStructuralLayer
from app.core.graph_intelligence.decision_engine import DecisionEngine as GraphDecisionEngine

from app.core.decision.engine import DecisionEngine as CoreDecisionEngine


class PredictiveIntelligenceLayer:

    VERSION = "6.9.5"


    def __init__(self):

        self.predictor = GraphEvolutionPredictor()

        self.structural = PredictiveStructuralLayer()

        self.graph_decision = GraphDecisionEngine()

        self.decision = CoreDecisionEngine()



    def process(
        self,
        signature,
        fusion,
        state,
        context=None,
        causal=None,
        risk=None,
        simulation=None,
        knowledge=None,
        history=None
    ):


        prediction = self.predictor.predict(
            signature
        )


        structural_prediction = self.structural.predict(
            fusion,
            history
        )


        intelligence = {

            "signature": signature,

            "prediction": prediction,

            "structural_prediction": structural_prediction

        }


        evolution_decision = self.graph_decision.analyze(
            intelligence,
            prediction,
            structural_prediction
        )


        final_decision = self.decision.decide(
            state,
            context,
            causal,
            risk,
            simulation,
            knowledge
        )


        return {

            "version": self.VERSION,

            "status": "PREDICTIVE_INTELLIGENCE_ACTIVE",

            "prediction": prediction,

            "structural_prediction": structural_prediction,

            "evolution_decision": evolution_decision,

            "decision": final_decision

        }
