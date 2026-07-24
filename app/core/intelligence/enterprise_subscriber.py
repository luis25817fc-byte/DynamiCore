class EnterpriseSubscriber:
    """
    DLIS-055-R1
    Enterprise Intelligence Subscriber Contract

    Consumer controlado de eventos Enterprise.
    """

    VERSION = "1.1"


    def __init__(
        self,
        name,
        handler,
        event_types=None
    ):

        self.name = name

        self.handler = handler

        self.event_types = (
            event_types
            if event_types
            else []
        )

        self.active = True

        self.processed_events = 0

        self.failed_events = 0



    def accepts(self, event):

        if not self.active:

            return False


        if not self.event_types:

            return True


        return event.event_type in self.event_types



    def process(self, event):

        if not self.accepts(event):

            return {

                "processed": False,

                "reason":
                    "EVENT_NOT_ACCEPTED"

            }


        try:

            result = self.handler(event)

            self.processed_events += 1


            return {

                "processed": True,

                "subscriber":
                    self.name,

                "result":
                    result

            }


        except Exception as error:

            self.failed_events += 1


            return {

                "processed": False,

                "subscriber":
                    self.name,

                "error":
                    str(error)

            }



    def activate(self):

        self.active = True



    def deactivate(self):

        self.active = False



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "name":
                self.name,

            "active":
                self.active,

            "processed_events":
                self.processed_events,

            "failed_events":
                self.failed_events

        }