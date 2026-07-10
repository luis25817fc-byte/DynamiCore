

class FeedbackEngine:


    def evaluate(
        self,
        decision,
        before,
        after
    ):


        improvement = 0


        if before and after:

            before_risk = before.get(
                "risk_score",
                0
            )

            after_risk = after.get(
                "risk_score",
                0
            )


            improvement = (
                before_risk -
                after_risk
            )



        if improvement > 0:

            outcome = "successful"

        elif improvement < 0:

            outcome = "failed"

        else:

            outcome = "neutral"



        return {


            "decision":

                decision.get(
                    "decision",
                    "unknown"
                ),


            "outcome":

                outcome,


            "impact":

                improvement,


            "learn":

                outcome == "successful"

        }

