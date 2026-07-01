from .graph import FunctionalGraph
from .cycles import CycleDetector
from .basins import BasinAnalyzer
from .entropy import Entropy
from .metrics import StructuralMetrics


class DynamiCore:
    def __init__(self, system):
        self.system = system

        self.graph = FunctionalGraph(system)
        self.cycles = CycleDetector(system)
        self.basins = BasinAnalyzer(system, self.cycles)

        self.entropy = Entropy
        self.metrics = StructuralMetrics

    def analyze(self):
        entropy_value = float(self.entropy.shannon(self.system))

        def safe(obj):
            if hasattr(obj, "summary"):
                return obj.summary()
            if hasattr(obj, "compute"):
                return obj.compute()
            return str(obj)

        basins = safe(self.basins)
        if not isinstance(basins, dict):
            basins = {}

        return {
            "system": self.system,

            "structure": {
                "graph": safe(self.graph),
                "cycles": safe(self.cycles),
                "basins": basins,
            },

            "information": {
                "entropy": entropy_value,
                "coherence": float(self.metrics.coherence(basins, len(self.system)))
            },

            "meta": {
                "size": len(self.system),
                "status": "stable"
            }
            }
