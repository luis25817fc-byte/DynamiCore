import math
from collections import Counter
import statistics


class DynamiCore:
    def __init__(self, system):
        self.system = system

    # =========================
    # 🔥 ENTROPÍA ACOPLADA
    # =========================
    def entropy(self):
        if not self.system:
            return 0.0

        counts = Counter(self.system)
        total = len(self.system)

        base_entropy = 0.0
        for c in counts.values():
            p = c / total
            base_entropy -= p * math.log2(p)

        # 🔥 acoplamiento dinámico real
        variance = statistics.pstdev(self.system) if len(self.system) > 1 else 0.0
        return base_entropy * (1 + math.tanh(variance))

    # =========================
    # 🔥 COHERENCIA (ESTABILIDAD)
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
    # 🔥 BASINS NO LINEALES (PRO REAL)
    # =========================
    def basins(self):
        if not self.system:
            return {}

        result = Counter()
        n = len(self.system)

        for i, x in enumerate(self.system):
            x = float(x)

            # 🔥 dinámica tipo sistema complejo
            value = (
                math.sin(x * 1.7 + i * 0.5) * 3 +
                math.cos(x * 0.9 - i * 0.3) * 2 +
                (x ** 2) * 0.07 +
                math.tanh(x + i) * 5 +
                n
            )

            basin_id = int(abs(value)) % 7
            result[f"basin_{basin_id}"] += 1

        return dict(result)

    # =========================
    # OUTPUT FINAL
    # =========================
    def analyze(self):
        return {
            "entropy": self.entropy(),
            "coherence": self.coherence(),
            "basins": self.basins()
        }
