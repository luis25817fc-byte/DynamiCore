
class CalibrationEngine:


    def __init__(self):

        self.history = []



    def calibrate(
        self,
        decision,
        feedback
    ):

        score = decision.get(
            "decision_score",
            0
        )


        if not feedback:

            return {
                "calibrated": False,
                "score": score,
                "reason": "no_feedback"
            }


        outcome = feedback.get(
            "outcome",
            "unknown"
        )


        impact = feedback.get(
            "impact",
            0
        )


        adjustment = 0


        if outcome == "successful":

            adjustment = abs(impact) * 0.2
            reason = "positive_learning"


        elif outcome == "failed":

            adjustment = -abs(impact) * 0.2
            reason = "negative_learning"


        else:

            reason = "neutral_learning"



        new_score = score + adjustment


        if new_score < 0:

            new_score = 0


        if new_score > 1:

            new_score = 1



        result = {

            "calibrated": True,

            "original_score": score,

            "adjusted_score":
                round(
                    new_score,
                    3
                ),

            "adjustment":
                round(
                    adjustment,
                    3
                ),

            "reason": reason

        }


        self.history.append(
            result
        )


        return result
