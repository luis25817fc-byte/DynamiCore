from datetime import datetime, timezone
from typing import List, Dict, Any


class TensorFusion:
    """
    DLIS-056.1

    Tensor Fusion Core

    Combina múltiples representaciones tensoriales
    en un estado cognitivo unificado.
    """

    VERSION = "1.0"



    def __init__(self):

        self.fusion_count = 0

        self.history = []



    def fuse(
        self,
        tensors: List[Dict[str, Any]]
    ):

        if not tensors:

            raise ValueError(
                "TensorFusion requires tensors"
            )


        values = []

        sources = []


        for tensor_state in tensors:

            tensor = tensor_state.get(
                "tensor",
                {}
            )


            tensor_values = tensor.get(
                "values",
                []
            )


            values.extend(
                tensor_values
            )


            sources.append(
                tensor_state.get(
                    "source_module"
                )
            )



        fused = {

            "fusion_id":

                self.fusion_count + 1,


            "timestamp":

                datetime.now(
                    timezone.utc
                ).isoformat(),


            "sources":

                sources,


            "tensor":

            {

                "dimensions":

                    len(values),


                "values":

                    values

            },


            "cognitive_score":

                self._score(values),


            "version":

                self.VERSION

        }


        self.fusion_count += 1


        self.history.append(
            fused
        )


        return fused



    def _score(self, values):

        if not values:

            return 0.0


        return sum(values) / len(values)



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "fusion_count":
                self.fusion_count,

            "history_size":
                len(self.history)

        }