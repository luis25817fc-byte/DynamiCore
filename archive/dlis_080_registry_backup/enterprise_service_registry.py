from datetime import datetime, timezone


class EnterpriseServiceRegistry:
    """
    DLIS-066B.2

    Enterprise Service Registry

    Catálogo central de servicios
    conectados al Runtime Kernel.
    """

    VERSION = "2.0"


    def __init__(self):

        self.services = {}


    def register(
        self,
        name,
        adapter
    ):

        self.services[name] = {

            "adapter": adapter,

            "registered_at":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        return {

            "service":
                name,

            "registered":
                True,

            "version":
                self.VERSION

        }


    def get(
        self,
        name
    ):

        if name not in self.services:

            raise KeyError(
                f"Service not found: {name}"
            )


        return self.services[name]["adapter"]


    def list_services(self):

        return list(
            self.services.keys()
        )


    def health_report(self):

        report = {}


        for name, data in self.services.items():

            report[name] = (
                data["adapter"].health()
            )


        return report


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "services":
                len(self.services),

            "registry":
                self.list_services()

        }



# ======================================================
# DLIS-078-A001
# Canonical Registry Instance
# ======================================================

enterprise_service_registry = EnterpriseServiceRegistry()
