from datetime import datetime, timezone



class EnterpriseAdaptivePolicy:
    """
    DLIS-064

    Enterprise Adaptive Policy Engine

    Convierte memoria estratégica
    en políticas adaptativas.
    """

    VERSION = "1.0"



    def __init__(self):

        self.policies = 0

        self.history = []



    def generate(
        self,
        strategy_memory
    ):


        memories = strategy_memory or []


        if memories:

            best = max(

                memories,

                key=lambda x:
                    x.get(
                        "performance",
                        0
                    )

            )


            policy = {

                "mode":
                    "REINFORCED_STRATEGY",

                "preferred_strategy":
                    best.get(
                        "strategy"
                    ),

                "confidence":
                    best.get(
                        "performance",
                        0
                    )

            }


        else:

            policy = {

                "mode":
                    "BASELINE",

                "preferred_strategy":
                    None,

                "confidence":
                    0.0

            }



        result = {

            "policy_id":
                self.policies + 1,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "policy":
                policy,

            "version":
                self.VERSION

        }



        self.policies += 1


        self.history.append(
            result
        )


        return result



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "policies":
                self.policies,

            "history_size":
                len(self.history)

        }