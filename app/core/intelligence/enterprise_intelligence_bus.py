from .enterprise_event import EnterpriseEvent
from .enterprise_priority import EnterprisePriority
from .enterprise_router import EnterpriseRouter
from .enterprise_trace import EnterpriseTrace


class EnterpriseIntelligenceBus:

    """
    DLIS-055-R1

    Enterprise Intelligence Bus Lifecycle Manager
    """

    VERSION = "1.1"


    def __init__(self):

        self.router = EnterpriseRouter()

        self.trace = EnterpriseTrace()

        self.published_events = 0



    def register_subscriber(self, subscriber):

        return self.router.register(subscriber)



    def publish(
        self,
        event_type,
        source,
        payload,
        target=None,
        priority=EnterprisePriority.NORMAL,
        metadata=None
    ):


        event = EnterpriseEvent(

            event_type=event_type,

            source=source,

            payload=payload,

            target=target,

            priority=priority,

            metadata=metadata or {}

        )


        self.published_events += 1


        event.status = "ROUTED"


        deliveries = self.router.route(
            event
        )


        event.mark_processed()


        trace = self.trace.record(
            event
        )


        return {

            "event":
                event.to_dict(),

            "deliveries":
                deliveries,

            "trace":
                trace

        }



    def publish_event(self, event):

        self.published_events += 1


        event.status = "ROUTED"


        deliveries = self.router.route(
            event
        )


        event.mark_processed()


        trace = self.trace.record(
            event
        )


        return {

            "event":
                event.to_dict(),

            "deliveries":
                deliveries,

            "trace":
                trace

        }



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "published_events":
                self.published_events,

            "router":
                self.router.diagnostics(),

            "trace":
                self.trace.diagnostics()

        }