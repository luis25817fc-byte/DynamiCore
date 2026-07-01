from .graph import FunctionalGraph
from .cycles import CycleDetector
from .basins import BasinAnalyzer
from .entropy import Entropy
from .metrics import StructuralMetrics


class DynamiCore:
    def __init__(self, system):
        self.system = system

        # Graph
        self.graph = FunctionalGraph(system)

        # Cycle detection
        self.cycles = CycleDetector(system)

        # Basin analysis
        self.basins = BasinAnalyzer(system, self.cycles)

        # Entropy (la clase solo tiene métodos estáticos)
        self.entropy = Entropy

        # Metrics
        self.metrics = StructuralMetrics(system)

    def analyze(self):
        result = {
            "system": self.system,
        }

        # Graph
        if hasattr(self.graph, "summary"):
            result["graph"] = self.graph.summary()
        else:
            result["graph"] = self.graph

        # Cycles
        if hasattr(self.cycles, "summary"):
            result["cycles"] = self.cycles.summary()
        else:
            result["cycles"] = self.cycles

        # Basins
        if hasattr(self.basins, "summary"):
            result["basins"] = self.basins.summary()
        else:
            result["basins"] = self.basins

        # Shannon entropy
        result["entropy"] = Entropy.shannon(self.system)

        # Metrics
        if hasattr(self.metrics, "compute"):
            result["metrics"] = self.metrics.compute()
        elif hasattr(self.metrics, "summary"):
            result["metrics"] = self.metrics.summary()
        else:
            result["metrics"] = self.metrics

        return result
