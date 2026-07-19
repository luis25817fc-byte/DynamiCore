
"""
DynamiCore Enterprise State
Contrato oficial del motor
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict
import uuid


@dataclass
class DynamiCoreState:

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    engine: str = "DynamiCore Enterprise"

    version: str = "1.0.0-alpha"

    input_size: int = 0


    entropy: Dict[str, Any] = field(
        default_factory=dict
    )

    metrics: Dict[str, Any] = field(
        default_factory=dict
    )

    graph: Dict[str, Any] = field(
        default_factory=dict
    )

    cycles: list = field(
        default_factory=list
    )

    basins: list = field(
        default_factory=list
    )

    memory: Dict[str, Any] = field(
        default_factory=dict
    )


    diagnostics: Dict[str, Any] = field(
        default_factory=dict
    )


    def to_dict(self):

        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "engine": self.engine,
            "version": self.version,
            "input_size": self.input_size,
            "entropy": self.entropy,
            "metrics": self.metrics,
            "graph": self.graph,
            "cycles": self.cycles,
            "basins": self.basins,
            "memory": self.memory,
            "diagnostics": self.diagnostics
        }


    def summary(self):

        return {
            "H(k)": self.entropy.get("shannon"),
            "R(k)": self.metrics.get("R"),
            "ΔR(k)": self.metrics.get("delta_R"),
            "Ψ(k)": self.metrics.get("psi"),
            "D(k)": self.metrics.get("divergence"),
            "Cycles": len(self.cycles),
            "Basins": len(self.basins)
        }
