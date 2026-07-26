from datetime import datetime, timezone
import uuid


class EnterpriseAdaptiveControlLoop:
    """
    DLIS-066E.5

    Adaptive Cognitive Control Loop

    Evalúa resultados y genera
    señales de adaptación.
    """

    VERSION = "2.0"


    def __init__(self):

        self.adaptations = []


    def evaluate(
        self,
        previous_strategy,
        expected_outcome,
        actual_outcome
    ):

        if expected_outcome == actual_outcome:

            signal = "REINFORCE_STRATEGY"

        else:

            signal = "ADJUST_STRATEGY"


        adaptation = {

            "adaptation_id":
                str(uuid.uuid4()),

            "previous_strategy":
                previous_strategy,

            "expected_outcome":
                expected_outcome,

            "actual_outcome":
                actual_outcome,

            "adaptation_signal":
                signal,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        self.adaptations.append(
            adaptation
        )


        return adaptation



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "adaptations":
                len(
                    self.adaptations
                ),

            "status":
                "READY"

        }