from dataclasses import dataclass, asdict
from datetime import datetime, timezone


def timestamp():
    return datetime.now(timezone.utc).isoformat()


@dataclass
class AuditRecord:
    audit_id: str
    trace_id: str
    objective: str
    agents: list
    status: str = "STARTED"
    created: str = timestamp()

    def to_dict(self):
        return asdict(self)


@dataclass
class DecisionAuditRecord:
    decision_id: str
    trace_id: str
    decision: str
    confidence: float
    created: str = timestamp()

    def to_dict(self):
        return asdict(self)


@dataclass
class ResponseAuditRecord:
    response_id: str
    trace_id: str
    action: str
    priority: str
    status: str
    created: str = timestamp()

    def to_dict(self):
        return asdict(self)


@dataclass
class MemoryAuditRecord:
    memory_id: str
    trace_id: str
    outcome: str
    learning: str
    created: str = timestamp()

    def to_dict(self):
        return asdict(self)