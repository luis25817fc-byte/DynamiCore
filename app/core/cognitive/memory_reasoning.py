
from datetime import datetime, timezone


class MemoryReasoning:

    """
    DynamiCore Memory Assisted Reasoning
    DLIS-029
    """

    VERSION = "DLIS-029"


    def __init__(
        self,
        memory_layer=None
    ):

        self.memory_layer = memory_layer


    def analyze_history(
        self,
        objective
    ):

        if not self.memory_layer:

            return {

                "version":
                    self.VERSION,

                "history_available":
                    False,

                "matches":
                    0

            }


        result = (
            self.memory_layer
            .find_by_objective(
                objective
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

            "history_available":
                result["matches"] > 0,

            "matches":
                result["matches"],

            "historical_traces":
                result["traces"]

        }


    def enrich_reasoning(
        self,
        reasoning,
        objective
    ):

        history = self.analyze_history(
            objective
        )


        enriched = {

            "version":
                self.VERSION,

            "base_reasoning":
                reasoning,

            "memory_context":
                history,

            "memory_informed":
                history["history_available"]

        }


        return enriched
