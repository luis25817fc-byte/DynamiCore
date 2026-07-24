class EnterpriseRouter:
    """
    DLIS-055-R1
    Enterprise Event Routing Contract
    """

    VERSION = "1.1"


    def __init__(self):

        self.subscribers = {}

        self.routing_history = []



    def register(self, subscriber):

        self.subscribers[subscriber.name] = subscriber

        return subscriber.name



    def unregister(self, name):

        if name in self.subscribers:

            del self.subscribers[name]

            return True

        return False



    def route(self, event):

        deliveries = []


        for name, subscriber in self.subscribers.items():

            result = subscriber.process(event)


            deliveries.append({

                "subscriber":
                    name,

                "result":
                    result

            })


        route_record = {

            "event_id":
                event.event_id,

            "event_type":
                event.event_type.value,

            "deliveries":
                deliveries

        }


        self.routing_history.append(
            route_record
        )


        return deliveries



    def list_subscribers(self):

        return list(
            self.subscribers.keys()
        )



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "subscriber_count":
                len(self.subscribers),

            "routes":
                len(self.routing_history)

        }