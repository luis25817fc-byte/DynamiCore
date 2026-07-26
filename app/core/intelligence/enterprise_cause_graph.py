from datetime import datetime, timezone
from uuid import uuid4


class EnterpriseCauseGraph:
    """
    DLIS-065.2

    Enterprise Cause Graph Engine

    Construye una representación causal
    basada en nodos y relaciones dirigidas.
    """

    VERSION = "1.0"


    def __init__(self):

        self.nodes = {}
        self.edges = []
        self.history = []


    def add_node(
        self,
        node_type: str,
        name: str,
        evidence_id: str | None = None
    ):

        node_id = str(uuid4())

        node = {

            "node_id": node_id,

            "type": node_type,

            "name": name,

            "evidence_id": evidence_id,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION
        }

        self.nodes[node_id] = node

        self.history.append(node)

        return node


    def add_causal_relation(
        self,
        source_id: str,
        target_id: str,
        relation: str = "CAUSES",
        weight: float = 0.0,
        confidence: float = 0.0,
        evidence_id: str | None = None
    ):

        edge = {

            "edge_id":
                str(uuid4()),

            "source":
                source_id,

            "target":
                target_id,

            "relation":
                relation,

            "weight":
                weight,

            "confidence":
                confidence,

            "evidence_id":
                evidence_id,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION
        }

        self.edges.append(edge)

        return edge


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "nodes":
                len(self.nodes),

            "relations":
                len(self.edges),

            "history_size":
                len(self.history)

        }