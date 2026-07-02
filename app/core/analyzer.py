import math
import statistics
from collections import Counter


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

        base = 0.0
        for c in counts.values():
            p = c / total
            base -= p * math.log2(p)

        variance = statistics.pstdev(self.system) if len(self.system) > 1 else 0.0

        return base * (1 + math.tanh(variance))

    # =========================
    # 🔥 COHERENCIA ESTRUCTURAL
    # =========================
    def coherence(self):
        if len(self.system) < 2:
            return 0.0

        diffs = [
            abs(self.system[i] - self.system[i - 1])
            for i in range(1, len(self.system))
        ]

        return 1 / (1 + statistics.mean(diffs))

    # =========================
    # 🔥 CHAOS SCORE (VARIABILIDAD NORMALIZADA)
    # =========================
    def chaos_score(self):
        if len(self.system) < 3:
            return 0.0

        diffs = [
            abs(self.system[i] - self.system[i - 1])
            for i in range(1, len(self.system))
        ]

        var = statistics.pvariance(diffs)
        max_d = max(diffs) if diffs else 1

        return var / (max_d + 1e-9)

    # =========================
    # 🔥 LYPUNOV APROX (DISCRETO SIMPLIFICADO)
    # =========================
    def lyapunov_like(self):
        if len(self.system) < 3:
            return 0.0

        growth = 0.0

        for i in range(1, len(self.system)):
            if self.system[i - 1] == 0:
                continue

            ratio = abs(self.system[i] - self.system[i - 1]) / (abs(self.system[i - 1]) + 1e-9)
            growth += math.log(1 + ratio)

        return growth / len(self.system)

    # =========================
    # 🔥 BASINS DINÁMICOS NO LINEALES
    # =========================
    def basins(self):
        if not self.system:
            return {}

        result = Counter()
        n = len(self.system)

        for i, x in enumerate(self.system):
            x = float(x)

            value = (
                math.sin(x * 1.7 + i * 0.5) * 3 +
                math.cos(x * 0.9 - i * 0.3) * 2 +
                (x ** 2) * 0.07 +
                math.tanh(x + i) * 5 +
                math.sin(i * x * 0.2) * 2 +
                n
            )

            basin_id = int(abs(value)) % 6
            result[f"basin_{basin_id}"] += 1

        return dict(result)

    # =========================
    # 🔥 DETECCIÓN DE FASE
    # =========================
    def phase_state(self):
        chaos = self.chaos_score()
        coh = self.coherence()

        score = chaos * (1 - coh)

        if score < 0.15:
            return "ORDERED"
        elif score < 0.45:
            return "CRITICAL"
        else:
            return "CHAOTIC"

    # =========================
    # 🔥 OUTPUT FINAL (PAPER STYLE)
    # =========================
    def analyze(self):
        return {
            "entropy": self.entropy(),
            "coherence": self.coherence(),
            "chaos_score": self.chaos_score(),
            "lyapunov_like": self.lyapunov_like(),
            "phase_state": self.phase_state(),
            "basins": self.basins()
        }
