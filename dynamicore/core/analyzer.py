from .graph import FunctionalGraph
from .cycles import CycleDetector
from .basins import BasinAnalyzer
from .entropy import Entropy
from .metrics import StructuralMetrics


class DynamiCore:
    def __init__(self, system):
        self.system = system

        # Core components
        self.graph = FunctionalGraph(system)
        self.cycles = CycleDetector(system)
        self.basins = BasinAnalyzer(system, self.cycles)

        # Utility modules (static)
        self.entropy = Entropy
        self.metrics = StructuralMetrics

        # Precompute summaries (evita recalcular)
        self._graph_summary = self._safe(self.graph, "summary")
        self._cycle_summary = self._safe(self.cycles, "summary")
        self._basin_summary = self._safe(self.basins, "summary")

    def _safe(self, obj, method):
        if hasattr(obj, method):
            return getattr(obj, method)()
        return obj

    def analyze(self):
        entropy_value = self.entropy.shannon(self.system)

        basins = self._basin_summary if isinstance(self._basin_summary, dict) else {}

        coherence = self.metrics.coherence(
            basins,
            len(self.system)
        ) if basins else 0.0

        return {
            "system": self.system,

            "structure": {
                "graph": self._graph_summary,
                "cycles": self._cycle_summary,
                "basins": self._basin_summary,
            },

            "information": {
                "entropy": float(entropy_value),
                "coherence": float(coherence),
            },

            "meta": {
                "size": len(self.system),
                "status": "stable"
            }
        }

    def to_dict(self):
        return self.analyze()

    def to_json(self):
        import json
        return json.dumps(self.analyze(), indent=2)
