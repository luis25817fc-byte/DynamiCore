
class StructuralSignatureV2:

    VERSION = "6.5.0"

    def generate(self, graph):

        nodes = len(graph.get("nodes", []))
        edges = len(graph.get("edges", []))

        density = 0

        if nodes > 1:
            density = round(
                edges / (nodes * (nodes-1)),
                3
            )

        return {
            "version": self.VERSION,
            "nodes": nodes,
            "edges": edges,
            "density": density,
            "signature": hash(
                str(graph)
            )
        }
