from datetime import datetime, timezone


class EnterprisePolicyFeedback:
    """
    DLIS-064.1

    Enterprise Policy Feedback Loop

    Evalúa el desempeño de una política y
    genera una recomendación de ajuste.
    """

    VERSION = "1.0"

    def __init__(self):

        self.feedbacks = 0
        self.history = []


    def evaluate(
        self,
        policy,
        performance
    ):

        confidence = (
            policy.get("policy", {})
                  .get("confidence", 0.0)
        )

        if performance >= confidence:

            recommendation = "REINFORCE_POLICY"

        elif performance >= 0.60:

            recommendation = "ADJUST_POLICY"

        else:

            recommendation = "REPLACE_POLICY"


        result = {

            "feedback_id":
                self.feedbacks + 1,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "policy_id":
                policy.get("policy_id"),

            "performance":
                performance,

            "recommendation":
                recommendation,

            "version":
                self.VERSION

        }

        self.feedbacks += 1

        self.history.append(result)

        return result


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "feedbacks":
                self.feedbacks,

            "history_size":
                len(self.history)

        }