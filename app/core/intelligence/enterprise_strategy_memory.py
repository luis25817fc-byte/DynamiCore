from datetime import datetime, timezone



class EnterpriseStrategyMemory:
    """
    DLIS-063.1

    Strategy Memory & Adaptation Layer

    Guarda desempeño histórico
    de estrategias empresariales.
    """

    VERSION = "1.0"



    def __init__(self):

        self.entries = 0

        self.history = []



    def store(
        self,
        strategy,
        performance
    ):


        result = {

            "memory_id":
                self.entries + 1,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "strategy":
                strategy.get(
                    "strategy"
                ),

            "confidence":
                strategy.get(
                    "confidence",
                    0.0
                ),

            "performance":
                performance,

            "learning_signal":
                (
                    "REINFORCE"
                    if performance >= 0.75
                    else
                    "ADJUST"
                ),

            "version":
                self.VERSION

        }


        self.entries += 1


        self.history.append(
            result
        )


        return result



    def retrieve(self):

        return self.history



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "entries":
                self.entries,

            "history_size":
                len(self.history)

        }