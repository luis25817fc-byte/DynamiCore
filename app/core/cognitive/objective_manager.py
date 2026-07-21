from datetime import datetime, timezone


class ObjectiveManager:
    """
    DynamiCore Objective Manager
    V8.0
    """

    VERSION = "V8.0"


    def select(self, cognitive_state):

        confidence = (
            cognitive_state
            .get("confidence", {})
            .get("confidence", 0)
        )

        reasoning = (
            cognitive_state
            .get("reasoning", {})
            .get("hypotheses", [])
        )

        objective = "observe"

        priority = "low"


        if "HIGH_POTENTIAL" in reasoning:

            objective = "maximize_potential"

            priority = "high"


        elif "STRUCTURAL_STABILITY" in reasoning:

            objective = "preserve_stability"

            priority = "medium"


        elif confidence < 0.50:

            objective = "collect_information"

            priority = "medium"


        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "objective":
                objective,

            "priority":
                priority,

            "confidence":
                confidence

        }
