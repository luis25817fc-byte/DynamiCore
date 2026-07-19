
class EvolutionDiffEngine:

    VERSION = "6.5.0"

    def compare(self, previous, current):

        prev_nodes = len(previous.get("nodes", []))
        curr_nodes = len(current.get("nodes", []))

        prev_edges = len(previous.get("edges", []))
        curr_edges = len(current.get("edges", []))

        return {
            "node_delta": curr_nodes - prev_nodes,
            "edge_delta": curr_edges - prev_edges,
            "growth": curr_nodes + curr_edges - prev_nodes - prev_edges
        }
