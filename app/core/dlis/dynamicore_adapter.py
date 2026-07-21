
from datetime import datetime, timezone


class DynamiCoreAdapter:

    """
    DLIS-015

    Adapter layer between
    DynamiCoreEngine and DLIS runtime.
    """

    VERSION = "DLIS-015"


    def __init__(
        self,
        engine
    ):

        self.engine = engine



    def status(self):

        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "engine_type":
                type(
                    self.engine
                ).__name__,

            "connected":
                self.engine is not None

        }



    def analyze(
        self,
        state
    ):

        if self.engine is None:

            raise RuntimeError(
                "DynamiCore Engine missing"
            )


        output = self.engine.analyze(
            state
        )


        return {

            "version":
                self.VERSION,

            "status":
                "ENGINE_EXECUTED",

            "output":
                output

        }
