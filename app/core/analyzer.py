import math
from collections import Counter

class DynamiCore:

    def analyze(self, system: list):

        counts = Counter(system)
        n = len(system)

        # Entropy
        entropy = 0
        for c in counts.values():
            p = c / n
            entropy -= p * math.log2(p)

        # Coherence (simple stability metric)
        mean = sum(system) / n
        variance = sum((x - mean) ** 2 for x in system) / n
        coherence = 1 / (1 + variance)

        # Basins
        basins = {
            f"basin_{i}": counts[k]
            for i, k in enumerate(sorted(counts.keys()))
        }

        return {
            "entropy": round(entropy, 6),
            "coherence": round(coherence, 6),
            "basins": basins,
            "n": n
        }
