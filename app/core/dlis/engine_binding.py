
from datetime import datetime, timezone


class DLISEngineBinding:

    """
    DLIS-014

    Connects DynamiCore Engine
    with DLIS runtime pipeline.
    """

    VERSION = "DLIS-014"


    def __init__(
        self,
        engine=None
    ):

        self.engine = engine



    def bind(self):

        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "engine_connected":
                self.engine is not None,

            "binding_status":
                (
                    "BOUND"
                    if self.engine is not None
                    else
                    "WAITING"
                )

        }



    def execute(
        self,
        state
    ):

        if self.engine is None:

            return {

                "version":
                    self.VERSION,

                "status":
                    "NO_ENGINE"

            }


        result = self.engine.analyze(
            state
        )


        return {

            "version":
                self.VERSION,

            "status":
                "EXECUTED",

            "engine_output":
                result

        }
