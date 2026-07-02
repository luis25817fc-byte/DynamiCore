import math
from collections import Counter


class DynamiCore:
    """
    DynamiCore v3.0 — Deterministic Dynamical Basin Analyzer
    Estilo paper científico: entropy + coherence + basin mapping estable
    """

    def __init__(self, system: list[int]):
        if not isinstance(system, list):
            raise ValueError("System must be a list of integers")

        self.system = [int(x) for x in system]
        self.n = len(self.system)

    # =========================
    # ENTROPY (Shannon base 2)
    # =========================
    def entropy(self) -> float:
        counts = Counter(self.system)
        total = len(self.system)

        entropy = 0.0
        for c in counts.values():
            p = c / total
            entropy -= p * math.log2(p)

        return float(entropy)

    # =========================
    # COHERENCE (orden estructural normalizado)
    # =========================
    def coherence(self) -> float:
        if len(self.system) <= 1:
            return 1.0

        diffs = [
            abs(self.system[i] - self.system[i - 1])
            for i in range(1, len(self.system))
        ]

        max_diff = max(diffs) if diffs else 1.0
        avg_diff = sum(diffs) / len(diffs)

        return float(1.0 - (avg_diff / (max_diff + 1e-9)))

    # =========================
    # BASINS (cuencas dinámicas)
    # =========================
    def basins(self) -> dict:
        """
        Divide el sistema en atractores deterministas.
        Estilo: investigación (no Streamlit, no UI logic aquí)
        """
        k = min(5, max(3, self.n // 2 or 3))

        chunks = [[] for _ in range(k)]

        for i, v in enumerate(self.system):
            chunks[i % k].append(v)

        basin_map = {}
        for i, chunk in enumerate(chunks):
            if len(chunk) == 0:
                basin_map[f"basin_{i}"] = 0.0
                continue

            # estabilidad = promedio normalizado
            basin_value = sum(chunk) / (len(chunk) + 1e-9)

            # escala científica estable (0–2.0)
            basin_map[f"basin_{i}"] = round(float(basin_value % 2.0 + 1.0), 6)

        return basin_map

    # =========================
    # OUTPUT FINAL
    # =========================
    def analyze(self):
        return {
            "entropy": self.entropy(),
            "coherence": self.coherence(),
            "basins": self.basins()
        }
