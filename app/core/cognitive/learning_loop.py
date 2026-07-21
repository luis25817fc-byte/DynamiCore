
from datetime import datetime, timezone


class CognitiveLearningLoop:

    """
    DynamiCore Cognitive Learning Loop
    DLIS-030
    """

    VERSION = "DLIS-030"


    def __init__(
        self,
        memory_layer=None
    ):

        self.memory_layer = memory_layer


    def evaluate(
        self,
        objective,
        action,
        outcome
    ):

        history = []

        if self.memory_layer:

            history = (
                self.memory_layer
                .find_by_objective(
                    objective
                )
                .get(
                    "traces",
                    []
                )
            )


        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "objective":
                objective,

            "action":
                action,

            "outcome":
                outcome,

            "historical_comparison":

                len(history),

            "learning_signal":

                "POSITIVE"
                if outcome == "SUCCESS"
                else "ADJUST"

        }
