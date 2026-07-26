from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List
from uuid import uuid4


class Severity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class DecisionStatus(Enum):
    PROPOSED = "PROPOSED"
    APPROVED = "APPROVED"
    EXECUTED = "EXECUTED"
    REJECTED = "REJECTED"


@dataclass(slots=True)
class EnterpriseMetadata:
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    version: str = "2.0"


@dataclass(slots=True)
class TwinState:
    metadata: EnterpriseMetadata
    entropy: float
    resilience: float
    cognitive_score: float
    policy: str
    decision: str
    confidence: float


@dataclass(slots=True)
class Prediction:
    metadata: EnterpriseMetadata
    scenario: str
    score: float
    confidence: float


@dataclass(slots=True)
class Evidence:
    metadata: EnterpriseMetadata
    sources: Dict[str, Any]
    confidence: float


@dataclass(slots=True)
class Decision:
    metadata: EnterpriseMetadata
    action: str
    confidence: float
    status: DecisionStatus


@dataclass(slots=True)
class CausalRelation:
    metadata: EnterpriseMetadata
    cause: str
    effect: str
    weight: float
    confidence: float


@dataclass(slots=True)
class EnterpriseEvent:
    metadata: EnterpriseMetadata
    event_type: str
    payload: Dict[str, Any]


@dataclass(slots=True)
class SimulationResult:
    metadata: EnterpriseMetadata
    scenarios: List[Prediction]
    selected: Prediction