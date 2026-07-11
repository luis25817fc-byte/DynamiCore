# api/core/engine.py

import math
from collections import Counter

class DynamiCoreEngine:

    def analyze(self, system: list):

        if not system:
            return {
                "error": "empty input"
            }

        counts = Counter(system)
        n = len(system)

        entropy = sum(
            -(c / n) * math.log2(c / n)
            for c in counts.values()
        )

        mean = sum(system) / n
        variance = sum((x - mean) ** 2 for x in system) / n
        coherence = 1 / (1 + variance)

        return {
            "entropy": round(entropy, 6),
            "coherence": round(coherence, 6),
            "n": n
}
