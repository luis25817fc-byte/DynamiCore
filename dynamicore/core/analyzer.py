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
        self.basins = BasinAnalyzer(system)
        self.entropy = Entropy(system)
        self.metrics = StructuralMetrics(system)

    def analyze(self):
        return {
            "system": self.system,
            "graph": self.graph,
            "cycles": self.cycles,
            "basins": self.basins,
            "entropy": self.entropy,
            "metrics": self.metrics,
        }
