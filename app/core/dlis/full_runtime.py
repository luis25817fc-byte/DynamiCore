
from datetime import datetime, timezone


class DLISFullRuntime:

    VERSION = "DLIS-018"


    def __init__(
        self,
        adapter,
        validator,
        tensor_binding
    ):

        self.adapter = adapter
        self.validator = validator
        self.tensor_binding = tensor_binding


    def execute(
        self,
        state,
        actions=None
    ):

        actions = actions or [
            "PREDICT",
            "ADAPT",
            "DECIDE"
        ]


        if isinstance(state, dict):

            normalized_state = state.get(
                "state",
                state
            )

        else:

            normalized_state = state



        engine_status = self.adapter.status()


        engine_output = self.adapter.analyze(
            normalized_state
        )


        tensor = self.tensor_binding.build(
            engine_output
        )


        potential = tensor.get(
            "psi",
            0
        )

        pressure = tensor.get(
            "pressure",
            0
        )

        coherence = tensor.get(
            "omega",
            0
        )

        energy = tensor.get(
            "energy",
            0
        )

        curvature = tensor.get(
            "curvature",
            0
        )

        collapse = tensor.get(
            "collapse",
            0
        )


        delta_psi = potential


        validation = self.validator.validate(
            potential,
            pressure,
            coherence,
            delta_psi,
            collapse,
            energy,
            curvature
        )


        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "runtime":
                "ONLINE",

            "engine_connected":
                engine_status.get(
                    "connected",
                    False
                ),

            "dlis_tensor":
                {
                    "tensor":
                        tensor
                },

            "validation":
                validation,

            "routing":
                {
                    "prediction":
                        "PREDICT" in actions,

                    "adaptation":
                        "ADAPT" in actions,

                    "decision":
                        "DECIDE" in actions
                },

            "enterprise_ready":
                (
                    engine_status.get(
                        "connected",
                        False
                    )
                    and validation.get(
                        "runtime_ready",
                        False
                    )
                )
        }
