from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import Lock
from typing import Any


@dataclass(slots=True)
class TelemetryRecord:

    timestamp: str
    component: str
    metric: str
    value: Any
    metadata: dict = field(default_factory=dict)


class EnterpriseTelemetryLayer:

    VERSION = "DLIS-076.1"

    def __init__(self):
        self._records: list[TelemetryRecord] = []
        self._lock = Lock()

    def emit(
        self,
        component: str,
        metric: str,
        value: Any,
        metadata: dict | None = None,
    ) -> TelemetryRecord:

        record = TelemetryRecord(
            timestamp=datetime.now(timezone.utc).isoformat(),
            component=component,
            metric=metric,
            value=value,
            metadata=metadata or {},
        )

        with self._lock:
            self._records.append(record)

        return record

    def total_records(self) -> int:
        return len(self._records)

    def latest(self) -> TelemetryRecord | None:

        if not self._records:
            return None

        return self._records[-1]

    def export(self) -> list[dict]:

        return [
            {
                "timestamp": r.timestamp,
                "component": r.component,
                "metric": r.metric,
                "value": r.value,
                "metadata": r.metadata,
            }
            for r in self._records
        ]
