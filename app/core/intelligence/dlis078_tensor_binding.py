
"""
DLIS-078-A003

Tensor Fusion Binding

Responsibility:
- Register Tensor Fusion service
- Connect Tensor layer with Enterprise Registry
- No modification to Tensor Fusion internals
"""

from app.core.intelligence.enterprise_service_registry import (
    enterprise_service_registry
)


VERSION = "DLIS-078-A003"


class TensorFusionBinding:

    def __init__(
        self,
        tensor_fusion=None
    ):

        self.tensor_fusion = tensor_fusion


    def register(self):

        if self.tensor_fusion is None:

            raise ValueError(
                "Tensor Fusion instance required"
            )


        return enterprise_service_registry.register(
            "tensor_fusion",
            self.tensor_fusion
        )


    def health(self):

        return {

            "status":
                "healthy",

            "binding":
                VERSION

        }


def create_tensor_binding(
    tensor_fusion
):

    return TensorFusionBinding(
        tensor_fusion
    )
