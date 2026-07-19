
class EvolutionEngine:


    def compare(self, previous, current):

        if previous is None or current is None:
            return {
                "error": "missing_snapshot"
            }


        prev_metrics = previous["analysis"]
        curr_metrics = current["analysis"]


        prev_risk = prev_metrics["risk"]["risk_score"]
        curr_risk = curr_metrics["risk"]["risk_score"]


        risk_change = curr_risk - prev_risk


        prev_conf = prev_metrics["regime_analysis"]["confidence"]
        curr_conf = curr_metrics["regime_analysis"]["confidence"]


        confidence_change = curr_conf - prev_conf


        if risk_change > 0:
            trajectory = "degrading"

        elif risk_change < 0:
            trajectory = "improving"

        else:
            trajectory = "stable"


        return {
            "risk_change": risk_change,
            "confidence_change": confidence_change,
            "trajectory": trajectory
        }
