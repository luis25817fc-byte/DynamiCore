import math
from collections import Counter


class DynamiCore:
    def __init__(self, system: list[int]):
        # 🔥 asegurar que TODO sea entero limpio
        self.system = [int(x) for x in system]

    # =========================
    # ENTROPY (ROBUSTA)
    # =========================
    def _entropy(self, data):
        if not data:
            return 0.0

        counts = Counter(data)
        total = len(data)

        entropy = 0.0

        for c in counts.values():
            p = c / total

            # 🔥 protección contra log(0)
            if p > 0:
                entropy -= p * math.log2(p)

        return float(entropy)

    # =========================
    # COHERENCE SIMPLE
    # =========================
    def _coherence(self, data):
        if not data:
            return 0.0

        mean = sum(data) / len(data)

        # desviación normalizada
        variance = sum((x - mean) ** 2 for x in data) / len(data)

        return 1 / (1 + variance)

    # =========================
    # BASINS SIMULADOS (ESTABLE)
    # =========================
    def _basins(self, data):
        if not data:
            return {}

        result = Counter()

        for x in data:
            # 🔥 FIX CLAVE: evitar floats / negativos raros
            x = int(abs(x))

            basin_id = x % 3  # simple clustering estable
            result[f"basin_{basin_id}"] += 1

        return dict(result)

    # =========================
    # MAIN ANALYSIS
    # =========================
    def analyze(self):
        data = self.system

        return {
            "entropy": self._entropy(data),
            "coherence": self._coherence(data),
            "basins": self._basins(data)
        }
