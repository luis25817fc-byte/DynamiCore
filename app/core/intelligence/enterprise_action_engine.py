from datetime import datetime, timezone


class EnterpriseActionEngine:
    """
    DLIS-058.1

    Enterprise Action Layer

    Convierte decisiones Enterprise
    en acciones trazables.
    """

    VERSION = "1.0"



    def __init__(self):

        self.actions = 0

        self.history = []



    def execute(
        self,
        decision
    ):

        decision_type = decision.get(
            "decision"
        )


        if decision_type == "OPTIMIZE":

            action = "APPLY_OPTIMIZATION"


        elif decision_type == "ADAPT":

            action = "APPLY_ADAPTATION"


        else:

            action = "RUN_INVESTIGATION"



        result = {

            "action_id":
                self.actions + 1,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "action":
                action,

            "source_decision":
                decision.get(
                    "decision_id"
                ),

            "confidence":
                decision.get(
                    "confidence",
                    0.0
                ),

            "status":
                "GENERATED",

            "explanation":
            {

                "decision_rule":
                    decision.get(
                        "explanation"
                    )

            },

            "version":
                self.VERSION

        }


        self.actions += 1


        self.history.append(
            result
        )


        return result



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "actions":
                self.actions,

            "history_size":
                len(self.history)

        }