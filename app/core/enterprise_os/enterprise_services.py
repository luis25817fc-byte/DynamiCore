from threading import RLock
from copy import deepcopy

class EnterpriseServices:
    def __init__(self, lifecycle_manager=None, resource_manager=None,
                 health_monitor=None, telemetry=None):
        self._lock = RLock()
        self._services = {}
        self.lifecycle_manager = lifecycle_manager
        self.resource_manager = resource_manager
        self.health_monitor = health_monitor
        self.telemetry = telemetry

    def register(self, name, service, metadata=None):
        if not isinstance(name, str) or not name.strip() or service is None:
            raise ValueError("valid name and service required")
        with self._lock:
            if name in self._services:
                raise ValueError("service already registered")
            self._services[name] = {
                "instance": service, "metadata": deepcopy(metadata or {})}
        return self.get(name)

    def get(self, name):
        with self._lock:
            if name not in self._services:
                raise KeyError(name)
            item = self._services[name]
            return {"name": name, "instance": item["instance"],
                    "metadata": deepcopy(item["metadata"])}

    def require(self, name):
        return self.get(name)["instance"]

    def unregister(self, name):
        with self._lock:
            if name not in self._services:
                raise KeyError(name)
            return self._services.pop(name)["instance"]

    def list_services(self):
        with self._lock:
            return [{"name": n, "metadata": deepcopy(v["metadata"])}
                    for n, v in sorted(self._services.items())]

    def diagnostics(self):
        with self._lock:
            count = len(self._services)
        return {"status": "HEALTHY", "registered_services": count,
                "integrations": {
                    n: obj is not None for n, obj in (
                        ("lifecycle_manager", self.lifecycle_manager),
                        ("resource_manager", self.resource_manager),
                        ("health_monitor", self.health_monitor),
                        ("telemetry", self.telemetry))}}

EnterpriseServicesRegistry = EnterpriseServices
