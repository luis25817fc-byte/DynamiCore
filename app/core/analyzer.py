import math
from collections import Counter


class DynamiCore:

    def __init__(self, system: list[int]):
        self.system = system
        self.n = len(system)

    # =========================
    # 📊 ENTROPÍA REAL (SHANNON)
    # =========================
    def entropy(self):
        if self.n == 0:
            return 0.0

        counts = Counter(self.system)
        probs = [c / self.n for c in counts.values()]

        return -sum(p * math.log2(p) for p in probs if p > 0)

    # =========================
    # 🧠 COHERENCIA REAL (AUTOCORRELACIÓN SIMPLIFICADA)
    # =========================
    def coherence(self):
        if self.n <= 1:
            return 1.0

        mean = sum(self.system) / self.n

        numerator = sum(
            (self.system[i] - mean) * (self.system[i - 1] - mean)
            for i in range(1, self.n)
        )

        denominator = sum((x - mean) ** 2 for x in self.system) + 1e-9

        return max(-1, min(1, numerator / denominator))

    # =========================
    # 🧩 BASINS (CLUSTERING SIMPLE REAL)
    # =========================
    def basins(self, k=4):

        if self.n == 0:
            return {}

        min_v = min(self.system)
        max_v = max(self.system)
        span = max(max_v - min_v, 1)

        basins = {f"basin_{i}": 0 for i in range(k)}

        for x in self.system:
            idx = int(((x - min_v) / span) * (k - 1))
            basins[f"basin_{idx}"] += 1

        return basins

    # =========================
    # 🔥 CHANGE DETECTION (DINÁMICA REAL)
    # =========================
    def change_rate(self):

        if self.n <= 1:
            return 0.0

        changes = sum(
            1 for i in range(1, self.n)
            if self.system[i] != self.system[i - 1]
        )

        return changes / (self.n - 1)

    # =========================
    # 🌡 CHAOS INDEX (REAL COMPOSITE)
    # =========================
    def chaos(self, entropy_val, coherence_val, change_rate):

        # normalización estable SaaS
        return entropy_val * (1 + change_rate) * (1 - abs(coherence_val))

    # =========================
    # 🚀 MAIN API OUTPUT
    # =========================
    def analyze(self):

        entropy_val = self.entropy()
        coherence_val = self.coherence()
        basins_val = self.basins()
        change_val = self.change_rate()

        chaos_val = self.chaos(entropy_val, coherence_val, change_val)

        # fase del sistema (realista, no “místico”)
        if entropy_val < 1:
            phase = "ORDERED"
        elif entropy_val < 3:
            phase = "MIXED"
        else:
            phase = "HIGH_VARIABILITY"

        return {
            "entropy": round(entropy_val, 6),
            "coherence": round(coherence_val, 6),
            "change_rate": round(change_val, 6),
            "chaos": round(chaos_val, 6),
            "phase": phase,
            "basins": basins_val
            }
