from datetime import datetime, timezone
from typing import Callable, Dict, List, Any
from uuid import uuid4


class EnterpriseEventBus:
    """
    DLIS-066A.4

    Enterprise Event Bus

    Sistema central de comunicación
    entre dominios DynamiCore.
    """

    VERSION = "2.0"


    def __init__(self):

        self.subscribers: Dict[str, List[Callable]] = {}

        self.history = []


    def subscribe(
        self,
        event_type: str,
        handler: Callable
    ):

        if event_type not in self.subscribers:
            self.subscribers[event_type] = []

        self.subscribers[event_type].append(
            handler
        )


    def publish(
        self,
        event_type: str,
        payload: Dict[str, Any]
    ):

        event = {

            "event_id":
                str(uuid4()),

            "event_type":
                event_type,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "payload":
                payload,

            "version":
                self.VERSION

        }


        self.history.append(event)


        handlers = self.subscribers.get(
            event_type,
            []
        )


        responses = []

        for handler in handlers:

            responses.append(
                handler(event)
            )


        return {

            "event":
                event,

            "listeners":
                len(handlers),

            "responses":
                responses

        }


    def replay(self):

        return self.history.copy()


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "event_types":
                len(self.subscribers),

            "events":
                len(self.history),

            "subscribers":
                sum(
                    len(v)
                    for v in self.subscribers.values()
                )

        }