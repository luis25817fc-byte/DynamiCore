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

        # Cycles
        self.cycles = CycleDetector(system)

        # Basins
        self.basins = BasinAnalyzer(system, self.cycles)

        # Utility classes (métodos estáticos)
        self.entropy = Entropy
        self.metrics = StructuralMetrics

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

        # Entropy
        result["entropy"] = Entropy.shannon(self.system)

        # Structural metrics
        if hasattr(self.basins, "summary"):
            basin_summary = self.basins.summary()
            basins = basin_summary if isinstance(basin_summary, dict) else {}
        else:
            basins = {}

        result["coherence"] = (
            StructuralMetrics.coherence(basins, len(self.system))
            if basins
            else 0.0
        )

        return result
