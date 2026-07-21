from datetime import datetime, timezone


class ActionSelector:
    """
    DynamiCore Action Selector
    V8.0
    """

    VERSION = "V8.0"


    def select(self, cognitive_state):

        objective = (
            cognitive_state
            .get("objective", {})
            .get("objective", "observe")
        )

        actions = {

            "maximize_potential":
                "increase_structural_coherence",

            "preserve_stability":
                "maintain_current_state",

            "collect_information":
                "request_more_data",

            "observe":
                "monitor"
        }

        selected = actions.get(
            objective,
            "monitor"
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
                selected

        }
