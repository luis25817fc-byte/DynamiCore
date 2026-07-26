from datetime import datetime, timezone
from uuid import uuid4


class EnterpriseRootCauseAnalyzer:
    """
    DLIS-065.3

    Enterprise Root Cause Analyzer

    Analiza relaciones causales y determina
    causas dominantes dentro del Cause Graph.
    """

    VERSION = "1.0"


    def __init__(self):

        self.analyses = 0
        self.history = []


    def analyze(
        self,
        causal_relations: list,
        nodes: dict,
        evidence_id: str | None = None
    ):

        if not causal_relations:

            result = {

                "analysis_id":
                    str(uuid4()),

                "timestamp":
                    datetime.now(
                        timezone.utc
                    ).isoformat(),

                "status":
                    "NO_CAUSE_FOUND",

                "version":
                    self.VERSION
            }

            self.history.append(result)

            return result


        primary_relation = max(
            causal_relations,
            key=lambda x: x.get(
                "weight",
                0
            )
        )


        source_node = nodes.get(
            primary_relation["source"],
            {}
        )

        target_node = nodes.get(
            primary_relation["target"],
            {}
        )


        result = {

            "analysis_id":
                str(uuid4()),

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "primary_cause":
                source_node.get(
                    "name"
                ),

            "affected_component":
                target_node.get(
                    "name"
                ),

            "causal_weight":
                primary_relation.get(
                    "weight"
                ),

            "confidence":
                primary_relation.get(
                    "confidence"
                ),

            "evidence_id":
                evidence_id,

            "recommendation":
                "INVESTIGATE_PRIMARY_CAUSE",

            "version":
                self.VERSION
        }


        self.analyses += 1

        self.history.append(result)

        return result


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "analyses":
                self.analyses,

            "history_size":
                len(self.history)

        }