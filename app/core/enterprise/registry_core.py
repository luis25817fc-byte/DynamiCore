from datetime import datetime, timezone
import uuid


class RegistryCore:

    VERSION = "1.0"

    def __init__(self):
        self.connectors = {}
        self.modules = {}
        self.services = {}
        self.created = datetime.now(timezone.utc)

    def register_connector(self, name, domain, capabilities):
        item = {
            "registry_id": str(uuid.uuid4()),
            "name": name,
            "domain": domain,
            "capabilities": capabilities,
            "status": "REGISTERED",
            "version": self.VERSION
        }
        self.connectors[name] = item
        return item

    def diagnostics(self):
        return {
            "version": self.VERSION,
            "connectors": len(self.connectors),
            "status": "READY"
        }
    

registry_core = RegistryCore()
