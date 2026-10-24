"""EOS-008 Enterprise Lifecycle Manager."""
from copy import deepcopy
from datetime import datetime, timezone
from threading import RLock


class EnterpriseLifecycleManager:
    VERSION = "EOS-008"
    ACTIVE = {"STARTING", "RUNNING", "STOPPING"}

    def __init__(self, process_manager=None, runtime_supervisor=None,
                 event_bus=None):
        self.process_manager = process_manager
        self.runtime_supervisor = runtime_supervisor
        self.event_bus = event_bus
        self._lock = RLock()
        self._services = {}

    def register_service(self, name, metadata=None,
                         start_callback=None, stop_callback=None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if start_callback is not None and not callable(start_callback):
            raise TypeError("start_callback must be callable")
        if stop_callback is not None and not callable(stop_callback):
            raise TypeError("stop_callback must be callable")

        with self._lock:
            if name in self._services:
                raise ValueError("service already registered")

            if self.process_manager is not None:
                self.process_manager.register(name, metadata=metadata)

            self._services[name] = {
                "name": name,
                "state": "REGISTERED",
                "metadata": deepcopy(metadata or {}),
                "start_callback": start_callback,
                "stop_callback": stop_callback,
                "error": None,
                "updated_at": self._timestamp(),
            }

        self._emit("SERVICE_REGISTERED", name)
        return self.get_service(name)

    def start_service(self, name):
        with self._lock:
            service = self._require(name)
            if service["state"] == "RUNNING":
                return self.get_service(name)
            if service["state"] in self.ACTIVE:
                raise RuntimeError("service transition already in progress")
            service["state"] = "STARTING"
            service["error"] = None
            service["updated_at"] = self._timestamp()
            callback = service["start_callback"]

        try:
            if callback is not None:
                result = callback()
            elif self.process_manager is not None:
                result = self.process_manager.start(name)
            else:
                result = None
            if result is False:
                raise RuntimeError("start operation returned False")
        except Exception as exc:
            with self._lock:
                service = self._require(name)
                service["state"] = "FAILED"
                service["error"] = type(exc).__name__ + ": " + str(exc)
                service["updated_at"] = self._timestamp()
            self._emit("SERVICE_FAILED", name)
            raise

        with self._lock:
            service = self._require(name)
            service["state"] = "RUNNING"
            service["updated_at"] = self._timestamp()
            result = self._public(service)
        self._emit("SERVICE_STARTED", name)
        return result

    def stop_service(self, name):
        with self._lock:
            service = self._require(name)
            if service["state"] in ("REGISTERED", "STOPPED"):
                return self.get_service(name)
            if service["state"] not in ("RUNNING", "FAILED"):
                raise RuntimeError("service transition already in progress")
            service["state"] = "STOPPING"
            service["updated_at"] = self._timestamp()
            callback = service["stop_callback"]

        try:
            if callback is not None:
                result = callback()
            elif self.process_manager is not None:
                result = self.process_manager.stop(name)
            else:
                result = None
            if result is False:
                raise RuntimeError("stop operation returned False")
        except Exception as exc:
            with self._lock:
                service = self._require(name)
                service["state"] = "FAILED"
                service["error"] = type(exc).__name__ + ": " + str(exc)
                service["updated_at"] = self._timestamp()
            self._emit("SERVICE_FAILED", name)
            raise

        with self._lock:
            service = self._require(name)
            service["state"] = "STOPPED"
            service["error"] = None
            service["updated_at"] = self._timestamp()
            result = self._public(service)
        self._emit("SERVICE_STOPPED", name)
        return result

    def start_all(self):
        with self._lock:
            names = list(self._services)
        results = []
        for name in names:
            results.append(self.start_service(name))
        return results

    def stop_all(self):
        with self._lock:
            names = list(self._services)
        results = []
        for name in reversed(names):
            if self.get_service(name)["state"] in ("RUNNING", "FAILED"):
                results.append(self.stop_service(name))
        return results

    def get_service(self, name):
        with self._lock:
            return self._public(self._require(name))

    def list_services(self):
        with self._lock:
            return [self._public(item) for item in self._services.values()]

    def health(self):
        with self._lock:
            states = [item["state"] for item in self._services.values()]
        failed = states.count("FAILED")
        running = states.count("RUNNING")
        status = "UNHEALTHY" if failed else (
            "HEALTHY" if all(s in ("RUNNING", "STOPPED", "REGISTERED")
                             for s in states) else "DEGRADED"
        )
        return {
            "component": self.VERSION,
            "status": status,
            "services_total": len(states),
            "services_running": running,
            "services_failed": failed,
        }

    def diagnostics(self):
        result = {
            "component": self.VERSION,
            "timestamp_utc": self._timestamp(),
            "health": self.health(),
            "services": self.list_services(),
        }
        if self.runtime_supervisor is not None:
            inspect = getattr(self.runtime_supervisor, "inspect", None)
            if callable(inspect):
                try:
                    result["runtime_supervisor"] = inspect()
                except Exception as exc:
                    result["runtime_supervisor_error"] = (
                        type(exc).__name__ + ": " + str(exc)
                    )
        return result

    def _require(self, name):
        if name not in self._services:
            raise KeyError("unknown service: " + str(name))
        return self._services[name]

    @staticmethod
    def _timestamp():
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def _public(service):
        return {
            key: deepcopy(service[key])
            for key in ("name", "state", "metadata", "error", "updated_at")
        }

    def _emit(self, event_type, name):
        if self.event_bus is not None:
            try:
                self.event_bus.publish(event_type, {"name": name})
            except Exception:
                pass


LifecycleManager = EnterpriseLifecycleManager
