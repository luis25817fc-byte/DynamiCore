
class RegimeEngine:


    def analyze(self, predictive, risk):

        regime = "stable"
        transition = False


        acceleration = predictive.get(
            "acceleration",
            0
        )

        risk_score = risk.get(
            "risk_score",
            0
        )


        if risk_score >= 0.7:
            regime = "unstable"
            transition = True

        elif acceleration > 0:
            regime = "expanding"

        elif acceleration < 0:
            regime = "contracting"


        confidence = min(
            1.0,
            abs(acceleration) + risk_score
        )


        return {
            "regime": regime,
            "transition": transition,
            "confidence": round(confidence, 3)
        }
