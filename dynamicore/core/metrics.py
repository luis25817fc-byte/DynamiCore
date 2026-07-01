class StructuralMetrics:
    def coherence(self, basins, total):
        if total == 0:
            return 0.0

        if not basins:
            return 0.0

        return max(basins.values()) / total
