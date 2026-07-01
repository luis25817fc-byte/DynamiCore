# app/core/analyzer.py

from collections import defaultdict


class DynamiCore:
    def __init__(self, system: list[int]):
        self.system = system

    # =========================
    # MAIN ANALYSIS ENGINE
    # =========================
    def analyze(self):
        n = len(self.system)

        # 🔥 DETECT CYCLES (versión simple determinista)
        visited = set()
        cycles = []
        basins = defaultdict(int)

        def dfs(start):
            path = []
            current = start

            while current not in path:
                path.append(current)
                visited.add(current)

                # transición determinista
                current = self.system[current % n]

            cycle_start = path.index(current)
            cycle = path[cycle_start:]

            return cycle

        for i in range(n):
            if i not in visited:
                cycle = dfs(i)
                cycles.append(cycle)
                basins[str(tuple(cycle))] = len(cycle)

        # 🔥 ENTROPY SIMPLE (normalizada)
        total = sum(basins.values()) or 1
        probs = [v / total for v in basins.values()]
        entropy = -sum(p * (p).bit_length() for p in probs if p > 0)

        # 🔥 COHERENCE (heurística simple estable)
        coherence = len(cycles) / n if n else 0

        # 🔥 GRAPH SERIALIZABLE (IMPORTANTE)
        nodes = list(range(n))
        edges = []

        for i in range(n):
            edges.append({
                "from": i,
                "to": self.system[i % n]
            })

        return {
            "system": self.system,
            "cycles": cycles,
            "basins": dict(basins),
            "entropy": float(entropy),
            "coherence": float(coherence),

            # 👇 ESTO YA ES LO QUE STREAMLIT NECESITA
            "graph": {
                "nodes": nodes,
                "edges": edges
            }
            }
