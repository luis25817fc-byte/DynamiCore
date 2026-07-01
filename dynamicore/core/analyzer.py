from .graph import FunctionalGraph
from .cycles import CycleDetector
from .basins import BasinAnalyzer
from .entropy import Entropy
from .metrics import StructuralMetrics

class DynamiCore:
    def __init__(self, successor):
        self.graph = FunctionalGraph(successor)
        self.graph.validate()

    def analyze(self):
        cycles = CycleDetector(self.graph).detect()
        basins = BasinAnalyzer(self.graph, cycles).compute()

        H = Entropy.shannon(list(basins.values()))
        R = StructuralMetrics.coherence(basins, self.graph.n)

        return {
            "states": self.graph.n,
            "cycles": len(cycles),
            "cycle_lengths": [len(c) for c in cycles],
            "entropy": H,
            "coherence": R
        }
