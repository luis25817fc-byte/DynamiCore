from datetime import datetime, timezone


class FeedbackIntegrator:
    """
    DynamiCore Feedback Integrator
    V8.0
    """

    VERSION = "V8.0"


    def __init__(self):

        self.history = []


    def update(self, cognitive_state):

        action = (
            cognitive_state
            .get("action", {})
            .get("action", "monitor")
        )

        objective = (
            cognitive_state
            .get("objective", {})
            .get("objective", "observe")
        )

        confidence = (
            cognitive_state
            .get("confidence", {})
            .get("confidence", 0)
        )

        record = {

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "objective":
                objective,

            "action":
                action,

            "confidence":
                confidence

        }

        self.history.append(record)

        return {

            "version":
                self.VERSION,

            "stored": True,

            "history_size":
                len(self.history),

            "last_record":
                record

        }
