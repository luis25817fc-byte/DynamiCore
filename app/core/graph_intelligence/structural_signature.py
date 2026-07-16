
"""
DynamiCore V6.11.0
Structural Signature Intelligence Engine
"""


import hashlib
import json


class StructuralSignatureEngine:

    VERSION = "6.11.0"


    def generate(
        self,
        graph
    ):

        graph = graph or {}


        nodes = graph.get(
            "nodes",
            []
        )

        edges = graph.get(
            "edges",
            []
        )


        node_count = len(nodes)

        edge_count = len(edges)



        density = 0

        if node_count > 1:

            density = round(
                (2 * edge_count) /
                (node_count * (node_count - 1)),
                4
            )


        degree_map = {}


        for node in nodes:

            node_id = node.get(
                "id"
            )

            degree_map[node_id] = 0



        for edge in edges:

            source = edge.get(
                "source"
            )

            target = edge.get(
                "target"
            )


            if source in degree_map:

                degree_map[source] += 1


            if target in degree_map:

                degree_map[target] += 1



        average_degree = 0


        if degree_map:

            average_degree = round(
                sum(degree_map.values()) /
                len(degree_map),
                4
            )



        complexity = round(
            density *
            average_degree,
            4
        )


        stability_index = round(
            1 /
            (1 + complexity),
            4
        )



        raw_signature = {

            "nodes":
                node_count,

            "edges":
                edge_count,

            "density":
                density,

            "average_degree":
                average_degree,

            "complexity":
                complexity

        }



        signature_hash = hashlib.sha256(
            json.dumps(
                raw_signature,
                sort_keys=True
            ).encode()
        ).hexdigest()



        return {

            "version":
                self.VERSION,

            "nodes":
                node_count,

            "edges":
                edge_count,

            "density":
                density,

            "average_degree":
                average_degree,

            "structural_complexity":
                complexity,

            "stability_index":
                stability_index,

            "signature_hash":
                signature_hash,

            "status":
                "STRUCTURAL_SIGNATURE_ACTIVE"

        }
