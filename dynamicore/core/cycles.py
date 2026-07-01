class CycleDetector:
    def __init__(self, system):
        self.system = system

    def compute(self):
        visited = set()
        cycles = []

        for i in range(len(self.system)):
            if i not in visited:
                cycle = []
                j = i

                while j not in visited:
                    visited.add(j)
                    cycle.append(j)
                    j = self.system[j]

                if cycle:
                    cycles.append(cycle)

        return cycles
