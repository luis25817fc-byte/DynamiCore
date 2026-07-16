
class StructuralSignatureEngine:

    VERSION = "6.3.1"

    def generate(self, graph):

        graph = graph or {}

        nodes = graph.get("nodes", [])
        edges = graph.get("edges", [])

        degree = {}

        for edge in edges:
            s = edge.get("source")
            t = edge.get("target")

            if s:
                degree[s] = degree.get(s, 0) + 1

            if t:
                degree[t] = degree.get(t, 0) + 1

        node_count = len(nodes)
        edge_count = len(edges)

        density = (
            (2 * edge_count) /
            (node_count * (node_count - 1))
            if node_count > 1 else 0
        )

        average_degree = (
            (2 * edge_count) / node_count
            if node_count > 0 else 0
        )

        complexity = density * average_degree

        stability = 1 / (1 + abs(complexity))

        return {
            "version": self.VERSION,
            "nodes": node_count,
            "edges": edge_count,
            "degree_distribution": degree,
            "density": density,
            "average_degree": average_degree,
            "structural_complexity": complexity,
            "stability_index": stability
        }
