
from app.core.contracts import (
    IntelligenceState,
    IntelligencePrediction,
    IntelligenceDecision,
    build_report
)


class DynamiCoreIntelligenceOrchestrator:

    def __init__(self, version="7.1.1"):
        self.version = version


    def analyze(
        self,
        system_id,
        state_vector=None,
        metrics=None
    ):

        state = IntelligenceState(
            system_id=system_id,
            state_vector=state_vector or {},
            metrics=metrics or {}
        )

        prediction = self.predict(state)

        decision = self.decide(prediction)

        return build_report(
            state,
            prediction,
            decision,
            "ONLINE"
        )


    def predict(self, state):

        divergence = state.metrics.get(
            "divergence",
            0
        )

        risk = "LOW"

        if divergence > 0.7:
            risk = "HIGH"

        elif divergence > 0.4:
            risk = "MEDIUM"


        return IntelligencePrediction(
            system_id=state.system_id,
            risk_level=risk,
            transition_probability=divergence,
            confidence=0.95,
            early_warning=divergence > 0.5,
            explanation={
                "metrics": state.metrics
            }
        )


    def decide(self, prediction):

        action = "ALLOW_OPERATION"

        if prediction.early_warning:
            action = "REVIEW_REQUIRED"


        return IntelligenceDecision(
            action=action,
            risk=prediction.risk_level,
            confidence=prediction.confidence,
            reasoning=prediction.explanation
        )
