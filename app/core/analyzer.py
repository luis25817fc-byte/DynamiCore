import math
from collections import Counter


class DynamiCore:
    def __init__(self, system: list[int]):
        # 🔥 blindaje total contra floats
        self.system = []
        for x in system:
            try:
                self.system.append(int(float(x)))
            except:
                self.system.append(0)

    def _entropy(self, data):
        if not data:
            return 0.0

        c = Counter(data)
        n = len(data)

        ent = 0.0
        for v in c.values():
            p = v / n
            if p > 0:
                ent -= p * math.log2(p)

        return float(ent)

    def _coherence(self, data):
        if not data:
            return 0.0

        mean = sum(data) / len(data)
        var = sum((x - mean) ** 2 for x in data) / len(data)

        return 1 / (1 + var)

    def _basins(self, data):
        if not data:
            return {}

        out = Counter()

        for x in data:
            # 🔥 ELIMINA CUALQUIER POSIBLE FLOAT
            try:
                x = int(float(x))
            except:
                x = 0

            # 🔥 NUNCA bit_length, SOLO operación segura
            basin = abs(x) % 4
            out[f"basin_{basin}"] += 1

        return dict(out)

    def analyze(self):
        try:
            data = self.system

            return {
                "entropy": self._entropy(data),
                "coherence": self._coherence(data),
                "basins": self._basins(data)
            }

        except Exception as e:
            # 🔥 evita que Render rompa frontend
            return {
                "entropy": 0,
                "coherence": 0,
                "basins": {},
                "error": str(e)
        }
