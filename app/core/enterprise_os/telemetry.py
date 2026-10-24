from threading import RLock
from copy import deepcopy
from math import isfinite

class EnterpriseTelemetry:
    def __init__(self):
        self._lock = RLock()
        self._metrics = {}

    def _key(self, name, labels):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("metric name must be non-empty")
        labels = tuple(sorted((str(k), str(v)) for k, v in (labels or {}).items()))
        return name, labels

    def _ensure(self, key, kind):
        m = self._metrics.get(key)
        if m is None:
            m = {"name": key[0], "labels": dict(key[1]), "type": kind}
            if kind == "counter": m["value"] = 0
            elif kind == "gauge": m["value"] = 0
            else: m.update(count=0, total=0, min=None, max=None, last=None)
            self._metrics[key] = m
        if m["type"] != kind:
            raise ValueError("metric type conflict")
        return m

    def increment(self, name, amount=1, labels=None):
        if not isinstance(amount, (int, float)) or not isfinite(amount) or amount < 0:
            raise ValueError("counter increment must be finite and non-negative")
        with self._lock:
            m = self._ensure(self._key(name, labels), "counter")
            m["value"] += amount
            return deepcopy(m)

    def set_gauge(self, name, value, labels=None):
        if not isinstance(value, (int, float)) or not isfinite(value):
            raise ValueError("gauge value must be finite")
        with self._lock:
            m = self._ensure(self._key(name, labels), "gauge")
            m["value"] = value
            return deepcopy(m)

    def observe(self, name, value, labels=None):
        if not isinstance(value, (int, float)) or not isfinite(value):
            raise ValueError("observation must be finite")
        with self._lock:
            m = self._ensure(self._key(name, labels), "observation")
            m["count"] += 1
            m["total"] += value
            m["min"] = value if m["min"] is None else min(m["min"], value)
            m["max"] = value if m["max"] is None else max(m["max"], value)
            m["last"] = value
            return deepcopy(m)

    def snapshot(self):
        with self._lock:
            return {"metric_count": len(self._metrics),
                    "metrics": [deepcopy(v) for v in self._metrics.values()]}

    def reset(self, name=None):
        with self._lock:
            if name is None: self._metrics.clear()
            else:
                self._metrics = {k:v for k,v in self._metrics.items() if k[0] != name}

    def diagnostics(self):
        return {"status": "HEALTHY", "metric_count": self.snapshot()["metric_count"]}

Telemetry = EnterpriseTelemetry
