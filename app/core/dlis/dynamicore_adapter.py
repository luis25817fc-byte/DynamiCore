from datetime import datetime, timezone


class DynamiCoreAdapter:

    VERSION = "DLIS-015"


    def __init__(self, engine=None):

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
                type(self.engine).__name__
                if self.engine else None,

            "connected":
                self.engine is not None
        }


    def analyze(self, state):

        if self.engine is None:

            return {

                "status":
                    "NO_ENGINE",

                "system":
                    state
            }


        return self.engine.analyze(
            state
        )
