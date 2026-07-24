from datetime import datetime, timezone


class EnterpriseDecisionEngine:
    """
    DLIS-058

    Enterprise Decision Layer

    Convierte estados cognitivos en
    decisiones explicables.
    """

    VERSION = "1.0"



    def __init__(self):

        self.decisions = 0

        self.history = []



    def evaluate(
        self,
        cognitive_state
    ):

        score = cognitive_state.get(
            "cognitive_score",
            0.0
        )


        if score >= 0.75:

            decision = "OPTIMIZE"

        elif score >= 0.50:

            decision = "ADAPT"

        else:

            decision = "INVESTIGATE"



        result = {

            "decision_id":
                self.decisions + 1,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "decision":
                decision,

            "confidence":
                score,

            "source_state":
                cognitive_state.get(
                    "state_id"
                ),

            "explanation":
                {
                    "rule":
                        "cognitive_score_threshold",

                    "score":
                        score

                },

            "version":
                self.VERSION

        }


        self.decisions += 1


        self.history.append(
            result
        )


        return result



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "decisions":
                self.decisions,

            "history_size":
                len(self.history)

        }