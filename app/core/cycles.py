class CycleDetector:
    def __init__(self, system):
        self.system = system

    def compute(self):
        visited = set()
        cycles = []
        n = len(self.system)

        for i in range(n):
            if i not in visited:
                cycle = []
                j = i

                while j not in visited:
                    visited.add(j)
                    cycle.append(j)
                    j = self.system[j]

                cycles.append(cycle)

        return cycles
