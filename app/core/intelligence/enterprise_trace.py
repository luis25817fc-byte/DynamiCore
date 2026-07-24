from datetime import datetime, timezone


class EnterpriseTrace:
    """
    DLIS-055-R1

    Enterprise Final State Trace System
    """

    VERSION = "1.1"


    def __init__(self):

        self.events = []

        self.started_at = (
            datetime.now(timezone.utc).isoformat()
        )



    def record(
        self,
        event,
        processing_time=None
    ):

        if event.status != "PROCESSED":

            raise ValueError(
                "Trace requires finalized event state"
            )


        entry = {

            "event_id":
                event.event_id,

            "correlation_id":
                event.correlation_id,

            "event_type":
                event.event_type.value,

            "source":
                event.source,

            "status":
                event.status,

            "priority":
                event.priority.name,

            "timestamp":
                event.timestamp,

            "processing_time":
                processing_time,

            "payload":
                event.payload,

            "metadata":
                event.metadata

        }


        self.events.append(entry)


        return entry



    def get_history(self):

        return self.events



    def latest(self):

        if not self.events:

            return None

        return self.events[-1]



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "total_events":
                len(self.events),

            "started_at":
                self.started_at

        }