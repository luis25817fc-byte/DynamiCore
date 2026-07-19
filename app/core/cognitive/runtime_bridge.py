from datetime import datetime, timezone


class CognitiveRuntimeBridge:
    """
    DynamiCore Cognitive Runtime Bridge
    V8.0

    Conecta DLIS Runtime con Cognitive Engine.
    """

    VERSION = "V8.0"


    def __init__(
        self,
        cognitive_engine
    ):

        self.cognitive_engine = cognitive_engine


    def execute(
        self,
        runtime_output
    ):

        cognitive_result = (
            self.cognitive_engine.execute(
                runtime_output
            )
        )


        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "runtime_connected":
                True,

            "cognitive_output":
                cognitive_result

        }
