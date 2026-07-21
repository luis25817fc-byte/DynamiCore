

from datetime import datetime, timezone


class CognitiveStateVector:

    VERSION = "DLIS-051"


    def __init__(self):

        self.cycles = 0



    def build(self, cognitive_output):

        self.cycles += 1


        reasoning = cognitive_output.get(
            "reasoning",
            {}
        )


        confidence = cognitive_output.get(
            "confidence",
            {}
        )


        objective = cognitive_output.get(
            "objective",
            {}
        )


        action = cognitive_output.get(
            "action",
            {}
        )


        feedback = cognitive_output.get(
            "feedback",
            {}
        )


        score = reasoning.get(
            "score",
            0
        )


        coherence = confidence.get(
            "confidence",
            0
        )


        priority = objective.get(
            "priority",
            "low"
        )


        history = feedback.get(
            "history_size",
            0
        )


        return {


            "version":
                self.VERSION,


            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),


            "vector":

                {


                    "cognitive_potential":
                        score / 4.0,


                    "cognitive_coherence":
                        coherence,


                    "decision_pressure":
                        (
                            1.0
                            if priority == "high"
                            else
                            0.5
                            if priority == "medium"
                            else
                            0.1
                        ),


                    "learning_energy":
                        history,


                    "collapse_risk":
                        (
                            1 - coherence
                        )

                },


            "action":
                action.get(
                    "action",
                    "monitor"
                )

        }



    def status(self):

        return {

            "version":
                self.VERSION,

            "cycles":
                self.cycles,

            "status":
                "ONLINE"

        }

