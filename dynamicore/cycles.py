class CycleDetector:
    """
    Detecta ciclos en un sistema funcional representado como lista de transiciones.
    Ejemplo: system[i] = siguiente estado desde i
    """

    def __init__(self, system):
        self.system = system
        self.n = len(system)
        self.cycles = []
        self.visited = set()
        self._compute_cycles()

    def _compute_cycles(self):
        visited_global = set()

        for start in range(self.n):
            if start in visited_global:
                continue

            path = []
            current = start
            local_index = {}

            while current not in local_index and current not in visited_global:
                local_index[current] = len(path)
                path.append(current)
                current = self.system[current]

            # si encontramos ciclo
            if current in local_index:
                cycle_start = local_index[current]
                cycle = path[cycle_start:]
                self.cycles.append(cycle)

            visited_global.update(path)

    def get_cycles(self):
        return self.cycles

    def cycle_count(self):
        return len(self.cycles)

    def largest_cycle(self):
        if not self.cycles:
            return []
        return max(self.cycles, key=len)

    def summary(self):
        return {
            "cycle_count": len(self.cycles),
            "cycles": self.cycles,
            "largest_cycle": self.largest_cycle()
                }
