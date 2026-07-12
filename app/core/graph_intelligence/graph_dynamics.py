
class GraphDynamicsEngine:

    VERSION="6.3.0"

    def analyze(self, previous, current):

        previous = previous or {}
        current = current or {}

        prev_nodes=len(previous.get("nodes",[]))
        curr_nodes=len(current.get("nodes",[]))

        prev_edges=len(previous.get("edges",[]))
        curr_edges=len(current.get("edges",[]))

        node_growth=curr_nodes-prev_nodes
        edge_growth=curr_edges-prev_edges

        velocity=abs(node_growth)+abs(edge_growth)

        return {
            "version":self.VERSION,
            "previous_nodes":prev_nodes,
            "current_nodes":curr_nodes,
            "node_growth":node_growth,
            "edge_growth":edge_growth,
            "structural_velocity":velocity,
            "evolving":velocity>0
        }
