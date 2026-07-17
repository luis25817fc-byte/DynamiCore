
"""
DynamiCore V6.2.1
Graph Delta Engine
"""


class GraphDeltaEngine:

    VERSION = "6.2.1"


    def compare(self, previous, current):

        previous = previous or {}
        current = current or {}


        previous_nodes = {
            n.get("id")
            for n in previous.get("nodes", [])
        }

        current_nodes = {
            n.get("id")
            for n in current.get("nodes", [])
        }


        previous_edges = {
            (
                e.get("source"),
                e.get("target")
            )
            for e in previous.get("edges", [])
        }


        current_edges = {
            (
                e.get("source"),
                e.get("target")
            )
            for e in current.get("edges", [])
        }


        added_nodes = current_nodes - previous_nodes
        removed_nodes = previous_nodes - current_nodes

        added_edges = current_edges - previous_edges
        removed_edges = previous_edges - current_edges


        score = (
            len(added_nodes)
            +
            len(removed_nodes)
            +
            len(added_edges)
            +
            len(removed_edges)
        )


        return {

            "version": self.VERSION,

            "changed": score > 0,

            "delta": {

                "nodes_added":
                    list(added_nodes),

                "nodes_removed":
                    list(removed_nodes),

                "edges_added":
                    list(added_edges),

                "edges_removed":
                    list(removed_edges)

            },

            "change_score":
                score

        }
