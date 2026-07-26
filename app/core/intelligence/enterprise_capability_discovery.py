from datetime import datetime, timezone


class EnterpriseCapabilityDiscovery:
    """
    DLIS-066B.3

    Enterprise Capability Discovery Layer

    Descubrimiento y catálogo de capacidades
    disponibles dentro de DynamiCore.
    """

    VERSION = "2.0"


    def __init__(self):

        self.capabilities = {}


    def register_capability(
        self,
        service_name,
        capability,
        metadata=None
    ):

        if service_name not in self.capabilities:

            self.capabilities[service_name] = []


        entry = {

            "capability":
                capability,

            "metadata":
                metadata or {},

            "registered_at":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        self.capabilities[
            service_name
        ].append(entry)


        return {

            "service":
                service_name,

            "capability":
                capability,

            "registered":
                True

        }


    def discover(
        self,
        capability
    ):

        matches = []


        for service, items in self.capabilities.items():

            for item in items:

                if item["capability"] == capability:

                    matches.append({

                        "service":
                            service,

                        "capability":
                            capability,

                        "metadata":
                            item["metadata"]

                    })


        return matches



    def service_capabilities(
        self,
        service_name
    ):

        return self.capabilities.get(
            service_name,
            []
        )


    def diagnostics(self):

        total = sum(
            len(v)
            for v in self.capabilities.values()
        )


        return {

            "version":
                self.VERSION,

            "services":
                len(self.capabilities),

            "capabilities":
                total

        }