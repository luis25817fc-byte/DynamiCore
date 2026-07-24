from datetime import datetime, timezone
from typing import Dict, Any, List


class CognitiveTensorAdapter:
    """
    DLIS-056

    Cognitive Tensor Adapter

    Transforma eventos Enterprise en
    representaciones tensoriales cognitivas.
    """

    VERSION = "1.0"


    def __init__(self):

        self.processed = 0

        self.history = []



    def transform(self, event):

        tensor = self._extract_tensor(event)


        representation = {

            "tensor_id":
                event.event_id,

            "source_event":
                event.event_type.value,

            "source_module":
                event.source,

            "timestamp":
                datetime.now(timezone.utc).isoformat(),

            "tensor":
                tensor,

            "metadata":
                {
                    "adapter_version":
                        self.VERSION
                }

        }


        self.processed += 1


        self.history.append(
            representation
        )


        return representation



    def _extract_tensor(self, event):

        payload = event.payload


        values = []


        for value in payload.values():

            if isinstance(value, (int, float)):

                values.append(float(value))


        return {

            "dimensions":
                len(values),

            "values":
                values

        }



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "processed":
                self.processed,

            "history_size":
                len(self.history)

        }