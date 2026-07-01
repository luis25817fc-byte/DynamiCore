class BasinAnalyzer:
    def __init__(self, system, cycles):
        self.system = system
        self.cycles = cycles.compute()

    def compute(self):
        basins = {}

        for c in self.cycles:
            basins[tuple(c)] = len(c)

        return basins
