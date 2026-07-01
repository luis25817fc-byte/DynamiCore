class StructuralMetrics:
    @staticmethod
    def coherence(basins, total):
        if total == 0:
            return 0.0
        return max(basins.values()) / total
