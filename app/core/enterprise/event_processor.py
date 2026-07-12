
class EnterpriseEventProcessor:

    VERSION = "6.7.2"


    def __init__(self):

        self.processed = 0


    def process(
        self,
        event
    ):

        self.processed += 1

        event_type = event.get(
            "type",
            "UNKNOWN"
        )

        priority = (
            "HIGH"
            if event_type == "CRITICAL"
            else "NORMAL"
        )


        return {

            "version":
                self.VERSION,

            "processed":
                True,

            "event_number":
                self.processed,

            "event_type":
                event_type,

            "priority":
                priority
        }


    def status(self):

        return {

            "version":
                self.VERSION,

            "processed_events":
                self.processed,

            "status":
                "ACTIVE"
        }
