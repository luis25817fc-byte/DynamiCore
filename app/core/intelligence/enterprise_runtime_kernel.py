from datetime import datetime, timezone


class EnterpriseRuntimeKernel:
    """
    DLIS-066A.6

    Enterprise Runtime Kernel

    Núcleo operativo de DynamiCore Enterprise.
    """

    VERSION = "2.0"


    def __init__(
        self,
        container=None,
        event_bus=None,
        observability=None
    ):

        self.container = container

        self.event_bus = event_bus

        self.observability = observability

        self.services = {}

        self.status = "CREATED"


    def register_service(
        self,
        name,
        service
    ):

        self.services[name] = service

        return {

            "service":
                name,

            "registered":
                True

        }


    def start(self):

        self.status = "RUNNING"


        if self.observability:

            self.observability.record_event(
                "RUNTIME_STARTED",
                {
                    "kernel_version":
                        self.VERSION
                }
            )


        return {

            "status":
                self.status,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "services":
                len(self.services),

            "version":
                self.VERSION

        }


    def health_check(self):

        components = {

            "container":
                self.container is not None,

            "event_bus":
                self.event_bus is not None,

            "observability":
                self.observability is not None

        }


        return {

            "runtime":
                self.status,

            "components":
                components,

            "healthy":
                all(components.values()),

            "version":
                self.VERSION

        }


    def shutdown(self):

        self.status = "STOPPED"


        return {

            "status":
                self.status,

            "version":
                self.VERSION

        }


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "status":
                self.status,

            "services":
                list(
                    self.services.keys()
                )

        }