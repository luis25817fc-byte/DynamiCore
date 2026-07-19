from datetime import datetime, timezone


class ContextBuilder:
    """
    DynamiCore Context Builder
    V8.0
    """

    VERSION = "V8.0"


    def build(self, runtime_state):

        tensor = runtime_state.get(
            "dlis_tensor",
            {}
        )

        validation = runtime_state.get(
            "validation",
            {}
        )

        routing = runtime_state.get(
            "routing",
            {}
        )

        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "tensor":
                tensor,

            "validation":
                validation,

            "routing":
                routing,

            "enterprise_ready":
                runtime_state.get(
                    "enterprise_ready",
                    False
                )

        }
