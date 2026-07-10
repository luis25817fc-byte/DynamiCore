
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


        impact = abs(
