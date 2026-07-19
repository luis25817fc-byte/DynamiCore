
class StructuralIntelligenceFusion:

    VERSION = "6.5.3"

    def fuse(
        self,
        signature,
        evolution_metrics,
        transition_intelligence,
        graph_intelligence,
        decision
    ):

        recommendation = decision.get(
            "recommendation",
            {}
        )

        action = (
            decision.get("action")
            or recommendation.get("action")
            or decision.get("status")
            or "UNKNOWN"
        )

        return {
            "version": self.VERSION,
            "system_state": transition_intelligence.get(
                "state",
                "UNKNOWN"
            ),
            "evolution_pressure": evolution_metrics.get(
                "evolution_pressure",
                0
            ),
            "structural_density": signature.get(
                "density",
                0
            ),
            "graph_status": graph_intelligence,
            "recommended_action": action
        }
