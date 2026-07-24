from .cognitive_tensor_adapter import (
    CognitiveTensorAdapter
)

from .tensor_fusion import (
    TensorFusion
)



class CognitivePipeline:
    """
    DLIS-056.2

    Enterprise Cognitive Pipeline

    Event → Tensor → Fusion → Cognitive State
    """

    VERSION = "1.0"



    def __init__(self):

        self.adapter = CognitiveTensorAdapter()

        self.fusion = TensorFusion()

        self.processed_events = 0

        self.history = []



    def process_event(self, event):

        tensor_state = self.adapter.transform(
            event
        )


        cognitive_state = self.fusion.fuse(
            [
                tensor_state
            ]
        )


        self.processed_events += 1


        record = {

            "event_id":
                event.event_id,

            "tensor":
                tensor_state,

            "cognitive_state":
                cognitive_state

        }


        self.history.append(
            record
        )


        return cognitive_state



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "processed_events":
                self.processed_events,

            "adapter":
                self.adapter.diagnostics(),

            "fusion":
                self.fusion.diagnostics(),

            "history":
                len(self.history)

        }