class EnterpriseRuntimeBridge:
    """
    DLIS-057.2

    Enterprise Runtime Bridge

    Conecta Enterprise Intelligence Bus
    con Runtime Orchestrator.
    """

    VERSION = "1.0"



    def __init__(
        self,
        orchestrator
    ):

        self.orchestrator = orchestrator

        self.events_received = 0

        self.history = []



    def handle(
        self,
        event
    ):

        result = self.orchestrator.process_event(
            event
        )


        self.events_received += 1


        self.history.append(
            {
                "event_id":
                    event.event_id,

                "result":
                    result
            }
        )


        return result



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "events_received":
                self.events_received,

            "history_size":
                len(self.history)

        }