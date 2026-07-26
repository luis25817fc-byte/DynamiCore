from datetime import datetime, timezone
from uuid import uuid4


class EnterpriseInfluencePropagation:
    """
    DLIS-065.4

    Enterprise Influence Propagation Engine

    Analiza cómo una causa se propaga
    dentro de una estructura causal.
    """

    VERSION = "1.0"


    def __init__(self):

        self.propagations = 0
        self.history = []


    def propagate(
        self,
        source_node: str,
        relations: list,
        nodes: dict
    ):

        affected_nodes = []

        total_influence = 0.0


        for relation in relations:

            if relation.get("source") == source_node:

                target_id = relation.get("target")

                target = nodes.get(
                    target_id,
                    {}
                )

                influence = (
                    relation.get(
                        "weight",
                        0
                    )
                    *
                    relation.get(
                        "confidence",
                        0
                    )
                )


                affected_nodes.append(
                    {
                        "node_id": target_id,

                        "name":
                            target.get(
                                "name"
                            ),

                        "influence":
                            round(
                                influence,
                                4
                            )
                    }
                )


                total_influence += influence


        result = {

            "propagation_id":
                str(uuid4()),

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "source_node":
                source_node,

            "affected_nodes":
                affected_nodes,

            "impact_score":
                round(
                    total_influence,
                    4
                ),

            "affected_count":
                len(
                    affected_nodes
                ),

            "version":
                self.VERSION
        }


        self.propagations += 1

        self.history.append(
            result
        )

        return result


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "propagations":
                self.propagations,

            "history_size":
                len(
                    self.history
                )

        }