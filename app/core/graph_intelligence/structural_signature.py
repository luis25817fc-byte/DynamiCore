
class StructuralSignatureEngine:

    VERSION = "6.2"

    def generate(self, graph):

        graph = graph or {}

        nodes = graph.get("nodes", [])
        edges = graph.get("edges", [])

        degree = {}

        for edge in edges:

            s = edge.get("source")
            t = edge.get("target")

            if s:
                degree[s] = degree.get(s,0)+1

            if t:
                degree[t] = degree.get(t,0)+1

        density = (
            (2*len(edges)) /
            (len(nodes)*(len(nodes)-1))
            if len(nodes)>1 else 0
        )

        return {

            "version":"6.2",

            "nodes":len(nodes),

            "edges":len(edges),

            "degree_distribution":degree,

            "density":density

        }
