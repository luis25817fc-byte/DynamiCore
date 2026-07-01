class CycleDetector:
    def __init__(self, graph):
        self.graph = graph

    def detect(self):
        visited = set()
        cycles = []

        for start in self.graph.states():
            if start in visited:
                continue

            path = []
            index = {}
            node = start

            while node not in index and node not in visited:
                index[node] = len(path)
                path.append(node)
                node = self.graph.next_state(node)

            if node in index:
                cycles.append(path[index[node]:])

            visited.update(path)

        return cycles
