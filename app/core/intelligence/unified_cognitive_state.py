from datetime import datetime, timezone

from .cognitive_aggregator import (
    CognitiveAggregator
)

from .tensor_fusion import (
    TensorFusion
)



class UnifiedCognitiveState:
    """
    DLIS-056.4

    Unified Cognitive State Engine

    Multi-source tensor aggregation and fusion layer.
    """

    VERSION = "1.0"



    def __init__(self):

        self.aggregator = CognitiveAggregator()

        self.fusion = TensorFusion()

        self.cycles = 0

        self.history = []



    def ingest(
        self,
        source,
        tensor_state
    ):

        return self.aggregator.register_signal(
            source,
            tensor_state
        )



    def compute(self):

        tensors = self.aggregator.collect()


        if not tensors:

            raise ValueError(
                "No cognitive signals available"
            )


        fused_state = self.fusion.fuse(
            tensors
        )


        state = {

            "state_id":
                self.cycles + 1,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "sources":
                fused_state["sources"],

            "tensor":
                fused_state["tensor"],

            "cognitive_score":
                fused_state["cognitive_score"],

            "version":
                self.VERSION

        }


        self.history.append(
            state
        )


        self.cycles += 1


        self.aggregator.clear_cycle()


        return state



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "cycles":
                self.cycles,

            "history_size":
                len(self.history),

            "fusion":
                self.fusion.diagnostics()

        }