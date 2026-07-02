import math
import statistics
from collections import Counter


class DynamiCore:
    """
    🔬 DynamiCore v3.0 — Scientific Dynamical System Analyzer

    Modelo:
    - Sistema dinámico discreto determinista
    - Espacio de estados finito
    - Métricas de información + dinámica no lineal
    """

    def __init__(self, system):
        self.system = system or []

    # =========================
    # 🔥 ENTROPÍA NORMALIZADA
    # =========================
    def entropy(self):
        if not self.system:
            return 0.0

        counts = Counter(self.system)
        n = len(self.system)

        h = 0.0
        for c in counts.values():
            p = c / n
            h -= p * math.log2(p)

        # acoplamiento estructural (no linealidad)
        var = statistics.pstdev(self.system) if n > 1 else 0.0
        return h * (1 + math.tanh(var))

    # =========================
    # 🔥 COHERENCIA (ESTABILIDAD LOCAL)
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
    # 🔥 CHAOS SCORE (DISPERSIÓN DINÁMICA)
    # =========================
    def chaos_score(self):
        if len(self.system) < 3:
            return 0.0

        diffs = [
            abs(self.system[i] - self.system[i - 1])
            for i in range(1, len(self.system))
        ]

        var = statistics.pvariance(diffs)
        m = max(diffs) if diffs else 1

        return var / (m + 1e-9)

    # =========================
    # 🔥 LYPUNOV-LIKE EXPANSION RATE
    # =========================
    def lyapunov_like(self):
        if len(self.system) < 3:
            return 0.0

        growth = 0.0
        n = len(self.system)

        for i in range(1, n):
            prev = abs(self.system[i - 1])
            curr = abs(self.system[i])

            ratio = abs(curr - prev) / (prev + 1e-9)
            growth += math.log(1 + ratio)

        return growth / n

    # =========================
    # 🔥 BASINS (MAPA DE ATRACTORES NO LINEALES)
    # =========================
    def basins(self):
        if not self.system:
            return {}

        result = Counter()
        n = len(self.system)

        for i, x in enumerate(self.system):
            x = float(x)

            # dinámica no lineal acoplada
            value = (
                math.sin(x * 1.9 + i * 0.6) * 3.0 +
                math.cos(x * 0.7 - i * 0.4) * 2.5 +
                math.tanh(x + i) * 4.0 +
                (x ** 2) * 0.05 +
                math.sin(x * i * 0.1) * 2.0 +
                n
            )

            basin_id = int(abs(value)) % 6
            result[f"basin_{basin_id}"] += 1

        return dict(result)

    # =========================
    # 🔥 RÉGIMEN DINÁMICO (CLASIFICACIÓN DE FASE)
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
    # 🔥 ÍNDICE GLOBAL DE COMPLEJIDAD
    # =========================
    def complexity_index(self):
        ent = self.entropy()
        chaos = self.chaos_score()
        lyap = self.lyapunov_like()

        return (ent + chaos + lyap) / 3

    # =========================
    # 🔥 OUTPUT FINAL (FORMATO PAPER)
    # =========================
    def analyze(self):
        return {
            "entropy": self.entropy(),
            "coherence": self.coherence(),
            "chaos_score": self.chaos_score(),
            "lyapunov_like": self.lyapunov_like(),
            "complexity_index": self.complexity_index(),
            "phase_state": self.phase_state(),
            "basins": self.basins()
        }
