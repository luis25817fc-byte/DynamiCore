import math
from collections import Counter

class DynamiCore:

    def __init__(self, system):
        self.system = system

    def analyze(self):

        counts = Counter(self.system)
        n = len(self.system)

        entropy = 0
        for c in counts.values():
            p = c / n
            entropy -= p * math.log2(p)

        mean = sum(self.system) / n
        variance = sum((x - mean)**2 for x in self.system) / n

        coherence = 1 / (1 + variance)

        sorted_keys = sorted(counts.keys())

        basins = {
            f"basin_{i}": counts[k]
            for i, k in enumerate(sorted_keys)
        }

        return {
            "entropy": round(entropy, 6),
            "coherence": round(coherence, 6),
            "basins": basins
        }
