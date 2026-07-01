class BasinAnalyzer:
    def __init__(self, graph, cycles):
        self.graph = graph
        self.cycles = cycles

    def compute(self):
        basins = {}

        for c in self.cycles:
            basins[tuple(c)] = len(c)

        return basins
