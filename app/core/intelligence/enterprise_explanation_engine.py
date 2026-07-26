from datetime import datetime, timezone
from uuid import uuid4


class EnterpriseExplanationEngine:
    """
    DLIS-065.6

    Enterprise Explanation Intelligence Layer

    Construye explicaciones estructuradas
    combinando causalidad, impacto y
    escenarios alternativos.
    """

    VERSION = "1.0"


    def __init__(self):

        self.explanations = 0
        self.history = []


    def explain(
        self,
        root_cause: dict,
        influence: dict,
        counterfactual: dict
    ):

        result = {

            "explanation_id":
                str(uuid4()),

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "cause":
                root_cause.get(
                    "primary_cause"
                ),

            "affected_component":
                root_cause.get(
                    "affected_component"
                ),

            "impact_score":
                influence.get(
                    "impact_score"
                ),

            "alternative_difference":
                counterfactual.get(
                    "impact_difference"
                ),

            "confidence":
                min(
                    root_cause.get(
                        "confidence",
                        0
                    ),
                    counterfactual.get(
                        "confidence",
                        0
                    )
                ),

            "summary":

                "CAUSAL_EVENT_ANALYZED",

            "version":
                self.VERSION
        }


        self.explanations += 1

        self.history.append(
            result
        )

        return result


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "explanations":
                self.explanations,

            "history_size":
                len(
                    self.history
                )

        }