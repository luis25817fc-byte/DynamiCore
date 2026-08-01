from datetime import datetime, timezone
import uuid


class EnterpriseConnectorRegistry:

    VERSION = "1.0"


    def __init__(self):

        self.registry = {}


    def register(
        self,
        connector_name,
        domain,
        capabilities
    ):

        connector = {
            "registry_id": str(uuid.uuid4()),
            "name": connector_name,
            "domain": domain,
            "capabilities": capabilities,
            "status": "REGISTERED",
            "created": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }


        self.registry[connector_name] = connector

        return connector


    def discover(
        self,
        connector_name
    ):

        return self.registry.get(
            connector_name,
            {
                "status": "NOT_FOUND"
            }
        )


    def update_status(
        self,
        connector_name,
        status
    ):

        connector = self.registry.get(
            connector_name
        )


        if not connector:

            return {
                "status": "NOT_FOUND"
            }


        connector["status"] = status

        return connector


    def list_connectors(self):

        return list(
            self.registry.values()
        )


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "registered": len(self.registry),
            "status": "READY"
        }