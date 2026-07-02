import math
from collections import Counter


class DynamiCore:
    """
    DynamiCore Ultra Luxe v4.0
    Sistema dinámico + métricas tipo fintech / research lab
    """

    def __init__(self, system):
        self.system = [int(x) for x in system] if system else []
        self.n = len(self.system)

    # =========================
    # ENTROPÍA (SHANNON NORMALIZADA)
    # =========================
    def entropy(self):
        if self.n == 0:
            return 0.0

        counts = Counter(self.system)
        h = 0.0

        for c in counts.values():
            p = c / self.n
            h -= p * math.log2(p)

        return round(h, 6)

    # =========================
    # COHERENCIA (ESTABILIDAD SISTÉMICA)
    # =========================
    def coherence(self):
        if self.n <= 1:
            return 1.0

        diffs = [
            abs(self.system[i] - self.system[i - 1])
            for i in range(1, self.n)
        ]

        avg = sum(diffs) / len(diffs)
        max_d = max(diffs) if diffs else 1

        return round(1 - (avg / (max_d + 1e-9)), 6)

    # =========================
    # CHAOS INDEX (VOLATILIDAD)
    # =========================
    def chaos_index(self):
        if self.n <= 2:
            return 0.0

        diffs = [
            abs(self.system[i] - self.system[i - 1])
            for i in range(1, self.n)
        ]

        return round(sum(diffs) / (len(diffs) + 1e-9), 6)

    # =========================
    # BASINS (MODELO PRO - ESTILO FINTECH)
    # =========================
    def basins(self):
        if self.n == 0:
            return {}

        k = min(6, max(3, self.n // 2))

        buckets = {f"basin_{i}": [] for i in range(k)}

        for i, v in enumerate(self.system):
            idx = (v * (i + 3)) % k
            buckets[f"basin_{idx}"].append(v)

        result = {}

        for kname, vals in buckets.items():
            if len(vals) == 0:
                result[kname] = 0.0
            else:
                score = sum(vals) / len(vals)
                result[kname] = round(float(score), 6)

        return result

    # =========================
    # PHASE DETECTION (ESTILO PAPER + TRADING SYSTEM)
    # =========================
    def phase(self):
        c = self.coherence()
        e = self.entropy()

        score = (1 - c) * e

        if score < 1.5:
            return "ORDERED"
        elif score < 3.5:
            return "TRANSITIONAL"
        else:
            return "CHAOTIC"

    # =========================
    # OUTPUT FINAL SAAS
    # =========================
    def analyze(self):
        return {
            "entropy": self.entropy(),
            "coherence": self.coherence(),
            "chaos": self.chaos_index(),
            "phase": self.phase(),
            "basins": self.basins()
        }
