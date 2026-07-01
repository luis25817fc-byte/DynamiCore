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

        self.entropy = Entropy()
        self.metrics = StructuralMetrics()

    def analyze(self):
        cycles = self.cycles.compute()
        basins = self.basins.compute()

        entropy_value = self.entropy.shannon(self.system)
        coherence_value = self.metrics.coherence(basins, len(self.system))
result.pop("graph", None)

if "basins" in result:
    result["basins"] = {
        str(k): v
        for k, v in result["basins"].items()
    }

return result
        return {
            "system": self.system,
            "graph": str(self.graph),
            "cycles": cycles,
            "basins": basins,
            "entropy": float(entropy_value),
            "coherence": float(coherence_value),
        }
