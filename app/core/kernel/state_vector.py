
from dataclasses import dataclass
from datetime import datetime


@dataclass
class StateVector:

    entropy: float
    coherence: float
    dynamics: float
    potential: float
    divergence: float

    timestamp: str = None


    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()


    def to_dict(self):
        return {
            "H(k)": self.entropy,
            "R(k)": self.coherence,
            "ΔR(k)": self.dynamics,
            "Ψ(k)": self.potential,
            "D(k)": self.divergence,
            "timestamp": self.timestamp
        }
