
class ConfidenceEngine:


    def __init__(self):

        self.history = []



    def evaluate(

        self,

        decision,

        causal,

        feedback=None

    ):


        decision_score = decision.get(

            "decision_score",

            0

        )


        causal_confidence = causal.get(

            "confidence",

            0

        )



        feedback_score = 0



        if feedback:

            feedback_score = abs(

                feedback.get(

                    "impact",

                    0

                )

            )



        values = [

            decision_score,

            causal_confidence,

            feedback_score

        ]



        confidence = sum(

            values

        ) / len(

            values

        )



        result = {


            "confidence":

                round(

                    confidence,

                    3

                ),


            "decision":

                decision_score,


            "causal":

                causal_confidence,


            "feedback":

                feedback_score

        }



        if confidence >= 0.75:

            result["level"] = "high"


        elif confidence >= 0.4:

            result["level"] = "medium"


        else:

            result["level"] = "low"



        self.history.append(

            result

        )


        return result
