
"""
DynamiCore V7.1
Core Intelligence Contract

Central communication layer between:
Metrics
Prediction
Adaptation
Decision
Enterprise Runtime
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, Optional


@dataclass
class IntelligenceState:

    system_id: str

    timestamp: datetime = field(
        default_factory=datetime.utcnow
    )

    state_vector: Dict[str, Any] = field(
        default_factory=dict
    )

    metrics: Dict[str, float] = field(
        default_factory=dict
    )

    structural_signature: Optional[str] = None

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class IntelligencePrediction:

    system_id: str

    future_state: Dict[str, Any] = field(
        default_factory=dict
    )

    risk_level: str = "UNKNOWN"

    transition_probability: float = 0.0

    confidence: float = 0.0

    early_warning: bool = False

    explanation: Dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class IntelligenceDecision:

    action: str

    priority: str = "LOW"

    risk: str = "UNKNOWN"

    confidence: float = 0.0

    requires_confirmation: bool = True

    reasoning: Dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class IntelligenceReport:

    version: str = "7.1"

    state: Optional[IntelligenceState] = None

    prediction: Optional[IntelligencePrediction] = None

    decision: Optional[IntelligenceDecision] = None

    status: str = "INITIALIZED"


def build_report(
    state,
    prediction,
    decision,
    status="ACTIVE"
):

    return IntelligenceReport(
        state=state,
        prediction=prediction,
        decision=decision,
        status=status
    )
