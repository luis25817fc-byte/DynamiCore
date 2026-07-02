import math
from collections import Counter


class DynamiCore:

    def __init__(self, system: list[int]):
        self.system = system
        self.n = len(system)

    # =========================
    # 🔥 ENTROPY (SHANNON BASE 2)
    # =========================
    def entropy(self):
        if self.n == 0:
            return 0.0

        counts = Counter(self.system)
        probs = [c / self.n for c in counts.values()]

        return -sum(p * math.log2(p) for p in probs if p > 0)

    # =========================
    # 🧠 COHERENCE (NORMALIZED ORDER METRIC)
    # =========================
    def coherence(self):
        if self.n <= 1:
            return 1.0

        diffs = [
            abs(self.system[i] - self.system[i - 1])
            for i in range(1, self.n)
        ]

        avg_diff = sum(diffs) / len(diffs)

        # normalización estable 0-1
        return 1 / (1 + avg_diff)

    # =========================
    # 🌌 BASINS (CUENCAS DINÁMICAS)
    # =========================
    def basins(self):

        if self.n == 0:
            return {}

        max_val = max(self.system)
        min_val = min(self.system)

        # evitar división por cero
        range_val = max(max_val - min_val, 1)

        # 4 cuencas fijas (estable y vendible)
        basins = {"basin_0": 0, "basin_1": 0, "basin_2": 0, "basin_3": 0}

        for x in self.system:

            norm = (x - min_val) / range_val  # 0-1

            if norm < 0.25:
                basins["basin_0"] += 1
            elif norm < 0.5:
                basins["basin_1"] += 1
            elif norm < 0.75:
                basins["basin_2"] += 1
            else:
                basins["basin_3"] += 1

        return basins

    # =========================
    # 🧪 MAIN ENGINE
    # =========================
    def analyze(self):

        entropy_val = self.entropy()
        coherence_val = self.coherence()
        basins_val = self.basins()

        # =========================
        # 🧬 CHAOS INDEX (ESTABLE)
        # =========================
        chaos = entropy_val * (1 - coherence_val)

        # =========================
        # 🌡 PHASE DETECTION
        # =========================
        if entropy_val < 1:
            phase = "ORDERED"
        elif entropy_val < 3:
            phase = "TRANSITION"
        else:
            phase = "CHAOTIC"

        return {
            "entropy": float(entropy_val),
            "coherence": float(coherence_val),
            "chaos": float(chaos),
            "phase": phase,
            "basins": basins_val
        }
