
"""
DLIS-010
Structural Intelligence Fusion

Combines DLIS structural signals with
graph, prediction and decision layers.
"""


from datetime import datetime


class StructuralIntelligenceFusion:


    VERSION = "DLIS-010"


    def __init__(
        self,
        graph_intelligence=None,
        prediction_engine=None,
        decision_engine=None
    ):

        self.graph_intelligence = graph_intelligence
        self.prediction_engine = prediction_engine
        self.decision_engine = decision_engine



    def fuse(
        self,
        dlis_signal,
        graph_state=None,
        prediction=None,
        decision=None
    ):


        regime = dlis_signal.get(
            "regime",
            "UNKNOWN"
        )


        structural = dlis_signal.get(
            "structural_signal",
            {}
        )


        psi = structural.get(
            "potential",
            0
        )

        energy = structural.get(
            "energy",
            0
        )

        coherence = structural.get(
            "coherence",
            0
        )

        collapse = structural.get(
            "collapse",
            0
        )


        intelligence_score = (
            (psi * 0.3)
            +
            (energy * 0.3)
            +
            (coherence * 0.3)
            +
            ((1-collapse) * 0.1)
        )


        actions = []


        routing = dlis_signal.get(
            "routing",
            {}
        )


        if routing.get(
            "prediction_required"
        ):

            actions.append(
                "PREDICT"
            )


        if routing.get(
            "adaptation_required"
        ):

            actions.append(
                "ADAPT"
            )


        if routing.get(
            "decision_required"
        ):

            actions.append(
                "DECIDE"
            )


        return {

            "version":
                self.VERSION,


            "timestamp":
                datetime.utcnow().isoformat(),


            "structural_state":
                regime,


            "intelligence_score":
                round(
                    intelligence_score,
                    6
                ),


            "actions":
                actions,


            "graph_connected":
                graph_state is not None,


            "prediction_connected":
                prediction is not None,


            "decision_connected":
                decision is not None

        }
