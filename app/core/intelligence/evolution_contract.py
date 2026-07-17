
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any


@dataclass
class EvolutionReport:

    version: str = "7.2"

    system_id: str = ""

    timestamp: datetime = field(
        default_factory=datetime.utcnow
    )

    previous_state: Dict[str, Any] = field(
        default_factory=dict
    )

    current_state: Dict[str, Any] = field(
        default_factory=dict
    )

    delta: Dict[str, Any] = field(
        default_factory=dict
    )

    transition: str = "UNKNOWN"

    confidence: float = 0.0

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )
