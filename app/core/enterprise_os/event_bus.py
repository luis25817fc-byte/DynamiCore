from datetime import datetime, timezone


class EventBus:

    VERSION = "EOS-004"

    def __init__(self):

        self._subscribers = {}
        self._history = []

    def subscribe(
        self,
        event_type,
        handler
    ):

        if not callable(handler):

            raise TypeError(
                "Event handler must be callable"
            )

        self._subscribers.setdefault(
            event_type,
            []
        ).append(handler)

        return {
            "version": self.VERSION,
            "event_type": event_type,
            "subscribers": len(
                self._subscribers[event_type]
            )
        }

    def unsubscribe(
        self,
        event_type,
        handler
    ):

        handlers = self._subscribers.get(
            event_type,
            []
        )

        if handler not in handlers:
            return False

        handlers.remove(handler)

        if not handlers:

            self._subscribers.pop(
                event_type,
                None
            )

        return True

    def publish(
        self,
        event_type,
        payload=None
    ):

        event = {
            "event_type": event_type,
            "payload": (
                payload
                if payload is not None
                else {}
            ),
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self._history.append(event)

        results = []

        for handler in list(
            self._subscribers.get(
                event_type,
                []
            )
        ):

            results.append(
                handler(event)
            )

        return {
            "version": self.VERSION,
            "event": event,
            "delivered": len(results),
            "results": results
        }

    def history(
        self,
        event_type=None
    ):

        if event_type is None:

            return list(
                self._history
            )

        return [
            event
            for event in self._history
            if event["event_type"] == event_type
        ]

    def health(self):

        return {
            "version": self.VERSION,
            "status": "ONLINE",
            "event_types": len(
                self._subscribers
            ),
            "subscribers": sum(
                len(handlers)
                for handlers
                in self._subscribers.values()
            ),
            "events_processed": len(
                self._history
            )
        }
