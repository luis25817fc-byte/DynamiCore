from copy import deepcopy
from datetime import datetime, timezone
from threading import RLock


class EnterpriseHealthMonitor:
    VERSION = "EOS-007"
    HEALTHY_STATES = {"HEALTHY", "OK", "PASS", "AVAILABLE"}

    def __init__(self, event_bus=None):
        self._lock = RLock()
        self._checks = {}
        self._last_report = None
        self._event_bus = event_bus

    def register_check(self, name, callback, critical=True):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not callable(callback):
            raise TypeError("callback must be callable")
        with self._lock:
            if name in self._checks:
                raise ValueError("check already registered")
            self._checks[name] = {
                "callback": callback,
                "critical": bool(critical),
            }
        return True

    def unregister_check(self, name):
        with self._lock:
            if name not in self._checks:
                return False
            del self._checks[name]
            return True

    def run_checks(self):
        with self._lock:
            checks = dict(self._checks)

        results = {}
        for name, spec in checks.items():
            try:
                raw = spec["callback"]()
                if isinstance(raw, bool):
                    healthy = raw
                    state = "HEALTHY" if raw else "UNHEALTHY"
                    details = {}
                elif isinstance(raw, dict):
                    details = deepcopy(raw)
                    state = str(raw.get("status", "UNKNOWN")).upper()
                    healthy = bool(raw.get(
                        "healthy", state in self.HEALTHY_STATES
                    ))
                else:
                    raise TypeError(
                        "check must return bool or dict, got "
                        + type(raw).__name__
                    )
                results[name] = {
                    "status": state,
                    "healthy": healthy,
                    "critical": spec["critical"],
                    "details": details,
                }
            except Exception as exc:
                results[name] = {
                    "status": "ERROR",
                    "healthy": False,
                    "critical": spec["critical"],
                    "error": type(exc).__name__ + ": " + str(exc),
                }

        failed_critical = any(
            not item["healthy"] and item["critical"]
            for item in results.values()
        )
        failed_optional = any(
            not item["healthy"] and not item["critical"]
            for item in results.values()
        )
        overall = (
            "UNHEALTHY" if failed_critical
            else "DEGRADED" if failed_optional
            else "HEALTHY"
        )

        report = {
            "component": self.VERSION,
            "status": overall,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "checks_total": len(results),
            "checks_passed": sum(
                1 for item in results.values() if item["healthy"]
            ),
            "checks_failed": sum(
                1 for item in results.values() if not item["healthy"]
            ),
            "checks": results,
        }

        with self._lock:
            self._last_report = deepcopy(report)

        if self._event_bus is not None:
            try:
                self._event_bus.publish("HEALTH_REPORT", deepcopy(report))
            except Exception:
                # Monitoring must still return its report if event delivery fails.
                pass

        return deepcopy(report)

    def report(self):
        with self._lock:
            return deepcopy(self._last_report)

    def health(self):
        report = self.run_checks()
        return {
            "component": self.VERSION,
            "status": report["status"],
            "checks_total": report["checks_total"],
            "checks_passed": report["checks_passed"],
            "checks_failed": report["checks_failed"],
        }


HealthMonitor = EnterpriseHealthMonitor
