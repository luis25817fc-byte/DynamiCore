import math
from collections import Counter
import statistics


class DynamiCore:
    def __init__(self, system):
        self.system = system

    # =========================
    # ENTROPÍA (Shannon base 2)
    # =========================
    def entropy(self):
        if not self.system:
            return 0.0

        counts = Counter(self.system)
        total = len(self.system)

        ent = 0.0
        for c in counts.values():
            p = c / total
            ent -= p * math.log2(p)

        return ent

    # =========================
    # COHERENCIA (estructura global)
    # =========================
    def coherence(self):
        if len(self.system) < 2:
            return 0.0

        diffs = [
            abs(self.system[i] - self.system[i - 1])
            for i in range(1, len(self.system))
        ]

        mean_diff = statistics.mean(diffs)
        return 1 / (1 + mean_diff)

    # =========================
    # 🔥 BASINS NO LINEALES (VERSIÓN PRO)
    # =========================
    def basins(self):
        if not self.system:
            return {}

        result = Counter()
        n = len(self.system)

        for i, x in enumerate(self.system):
            x = float(x)

            # 🔥 dinámica no lineal tipo “paper”
            value = (
                math.sin(x * 1.7 + i) * 3 +
                math.cos(x * 0.9 - i * 0.3) * 2 +
                (x ** 2) * 0.05 +
                n
            )

            basin_id = int(abs(value)) % 7
            result[f"basin_{basin_id}"] += 1

        return dict(result)

    # =========================
    # OUTPUT PRINCIPAL
    # =========================
    def analyze(self):
        return {
            "entropy": self.entropy(),
            "coherence": self.coherence(),
            "basins": self.basins()
        }
