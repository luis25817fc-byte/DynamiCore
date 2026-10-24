"""EOS-006 Enterprise Resource Manager."""
from threading import RLock
from time import time


class EnterpriseResourceManager:
    VERSION = "EOS-006"

    def __init__(self):
        self._lock = RLock()
        self._resources = {}

    def register(self, name, capacity=1, metadata=None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if isinstance(capacity, bool) or not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("capacity must be a positive number")
        with self._lock:
            if name in self._resources:
                raise ValueError("resource already registered")
            self._resources[name] = {
                "capacity": capacity,
                "used": 0,
                "metadata": dict(metadata or {}),
                "created_at": time(),
            }
            return self.get(name)

    def acquire(self, name, amount=1):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("amount must be a positive number")
        with self._lock:
            item = self._require(name)
            if item["used"] + amount > item["capacity"]:
                return False
            item["used"] += amount
            return True

    def release(self, name, amount=1):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("amount must be a positive number")
        with self._lock:
            item = self._require(name)
            if amount > item["used"]:
                raise ValueError("release exceeds acquired amount")
            item["used"] -= amount
            return self.get(name)

    def get(self, name):
        with self._lock:
            item = self._require(name)
            return {
                "name": name,
                "capacity": item["capacity"],
                "used": item["used"],
                "available": item["capacity"] - item["used"],
                "metadata": dict(item["metadata"]),
                "status": "EXHAUSTED" if item["used"] == item["capacity"] else "AVAILABLE",
            }

    def list_resources(self):
        with self._lock:
            return [self.get(name) for name in sorted(self._resources)]

    def remove(self, name):
        with self._lock:
            item = self._require(name)
            if item["used"] != 0:
                raise RuntimeError("cannot remove a resource while in use")
            del self._resources[name]
            return True

    def health(self):
        with self._lock:
            resources = list(self._resources.values())
            return {
                "component": self.VERSION,
                "status": "HEALTHY",
                "resource_count": len(resources),
                "capacity": sum(x["capacity"] for x in resources),
                "used": sum(x["used"] for x in resources),
            }

    def _require(self, name):
        if name not in self._resources:
            raise KeyError("unknown resource: " + str(name))
        return self._resources[name]


ResourceManager = EnterpriseResourceManager
