
"""
DynamiCore V6.11.0
Graph Delta Intelligence Engine
"""


class GraphDeltaEngine:

    VERSION = "6.11.0"


    def compare(
        self,
        previous,
        current
    ):

        previous = previous or {}

        current = current or {}


        previous_nodes = {
            n.get("id")
            for n in previous.get(
                "nodes",
                []
            )
        }


        current_nodes = {
            n.get("id")
            for n in current.get(
                "nodes",
                []
            )
        }


        previous_edges = {
            (
                e.get("source"),
                e.get("target")
            )
            for e in previous.get(
                "edges",
                []
            )
        }


        current_edges = {
            (
                e.get("source"),
                e.get("target")
            )
            for e in current.get(
                "edges",
                []
            )
        }



        added_nodes = (
            current_nodes -
            previous_nodes
        )


        removed_nodes = (
            previous_nodes -
            current_nodes
        )


        added_edges = (
            current_edges -
            previous_edges
        )


        removed_edges = (
            previous_edges -
            current_edges
        )


        node_variation = (
            len(added_nodes) +
            len(removed_nodes)
        )


        edge_variation = (
            len(added_edges) +
            len(removed_edges)
        )


        total_changes = (
            node_variation +
            edge_variation
        )


        max_size = max(
            len(previous_nodes) +
            len(previous_edges),
            len(current_nodes) +
            len(current_edges),
            1
        )


        structural_variation = round(
            total_changes / max_size,
            4
        )


        if structural_variation >= 0.7:

            pressure = "HIGH"

        elif structural_variation >= 0.3:

            pressure = "MEDIUM"

        else:

            pressure = "LOW"



        return {

            "version":
                self.VERSION,

            "added_nodes":
                list(added_nodes),

            "removed_nodes":
                list(removed_nodes),

            "added_edges":
                list(added_edges),

            "removed_edges":
                list(removed_edges),

            "nodes_changed":
                node_variation,

            "edges_changed":
                edge_variation,

            "total_changes":
                total_changes,

            "structural_variation":
                structural_variation,

            "topology_pressure":
                pressure

        }
