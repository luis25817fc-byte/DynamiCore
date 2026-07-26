from datetime import datetime, timezone
from uuid import uuid4


class EnterpriseDigitalTwin:
    """
    DLIS-066

    Enterprise Digital Twin Core

    Mantiene una representación viva del
    estado cognitivo del sistema.
    """

    VERSION = "1.0"


    def __init__(self):

        self.twin_id = str(uuid4())

        self.created = datetime.now(
            timezone.utc
        ).isoformat()

        self.current_state = {}

        self.event_history = []

        self.version = self.VERSION


    def update_state(
        self,
        state: dict
    ):

        self.current_state.update(state)

        self.event_history.append({

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "event":
                "STATE_UPDATED",

            "state":
                state

        })

        return self.snapshot()


    def snapshot(self):

        return {

            "twin_id":
                self.twin_id,

            "created":
                self.created,

            "current_state":
                self.current_state,

            "events":
                len(self.event_history),

            "version":
                self.version

        }


    def diagnostics(self):

        return {

            "version":
                self.version,

            "events":
                len(self.event_history),

            "state_variables":
                len(self.current_state)

        }