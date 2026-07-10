

class AdaptiveThresholdEngine:


    def __init__(self):

        self.version = "6.0"

        self.history = []



    def evaluate(

        self,

        confidence,

        impact=0,

        policy=None

    ):


        confidence = float(
            confidence or 0
        )


        impact = abs(
            float(
                impact or 0
            )
        )



        if confidence >= 0.75 and impact >= 0.5:

            action = "adapt"


        elif confidence >= 0.45:

            action = "learn"


        else:

            action = "observe"



        result = {


            "version":

                self.version,


            "action":

                action,


            "confidence":

                round(

                    confidence,

                    3

                ),


            "impact":

                round(

                    impact,

                    3

                ),


            "policy":

                policy or "unknown"

        }



        self.history.append(

            result

        )


        return result
