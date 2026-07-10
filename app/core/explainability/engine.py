
class ExplainabilityEngine:


    def generate(
        self,
        state,
        causal,
        decision
    ):


        evidence = []


        if state.coherence < 0.3:

            evidence.append(
                "coherence degradation detected"
            )


        if state.divergence > 0.5:

            evidence.append(
                "structural divergence increased"
            )


        if state.dynamics < 0:

            evidence.append(
                "negative system dynamics"
            )


        if not evidence:

            evidence.append(
                "no critical indicators detected"
            )



        confidence = causal.get(
            "confidence",
            0
        )



        return {


            "summary":
                "DynamiCore analysis explanation",


            "evidence":
                evidence,


            "cause":
                causal.get(
                    "cause",
                    "unknown"
                ),


            "decision":
                decision.get(
                    "decision",
                    "none"
                ),


            "priority":
                decision.get(
                    "priority",
                    "unknown"
                ),


            "confidence":
                confidence

        }
