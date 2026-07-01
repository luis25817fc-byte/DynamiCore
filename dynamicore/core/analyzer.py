from .graph import FunctionalGraph
from .cycles import CycleDetector
from .basins import BasinAnalyzer
from .entropy import Entropy
from .metrics import StructuralMetrics


class DynamiCore:
    def __init__(self, system):
        self.system = system

        # Graph layer
        self.graph = FunctionalGraph(system)

        # Cycle detection
        self.cycles = CycleDetector(system)

        # Basin analysis (DEPENDE de cycles)
        self.basins = BasinAnalyzer(system, self.cycles)

        # Entropy + metrics
        self.entropy = Entropy(system)
        self.metrics = StructuralMetrics(system)

    def analyze(self):
        return {
            "system": self.system,

            "graph": self.graph.summary() if hasattr(self.graph, "summary") else self.graph,

            "cycles": self.cycles.summary() if hasattr(self.cycles, "summary") else self.cycles,

            "basins": self.basins.summary() if hasattr(self.basins, "summary") else self.basins,

            "entropy": self.entropy.compute() if hasattr(self.entropy, "compute") else self.entropy,

            "metrics": self.metrics.compute() if hasattr(self.metrics, "compute") else self.metrics,
        }
