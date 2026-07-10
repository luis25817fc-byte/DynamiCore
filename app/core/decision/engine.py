

class DecisionEngine:


    def decide(
        self,
        state,
        context,
        causal,
        risk=None,
        simulation=None,
        knowledge=None
    ):


        score = 0.0


        reasons = []



        # ==========================
        # RISK ANALYSIS
        # ==========================

        if risk:

            risk_score = risk.get(
                "risk_score",
                0
            )

            score += risk_score

            if risk_score > 0.5:

                reasons.append(
                    "high_risk_detected"
                )



        # ==========================
        # STATE ANALYSIS
        # ==========================

        if state.divergence > 0.5:

            score += 0.3

            reasons.append(
                "structural_divergence"
            )


        if state.coherence < 0.3:

            score += 0.3

            reasons.append(
                "low_coherence"
            )


        if state.dynamics < 0:

            score += 0.2

            reasons.append(
                "negative_dynamics"
            )



        # ==========================
        # CAUSAL INTELLIGENCE
        # ==========================

        causal_strength = causal.get(
            "causal_strength",
            0
        )


        score += causal_strength * 0.2


        if causal_strength > 0.5:

            reasons.append(
                "strong_causal_signal"
            )



        # ==========================
        # SIMULATION IMPACT
        # ==========================

        if simulation:

            impact = simulation.get(
                "impact",
                0
            )


            if impact > 0:

                reasons.append(
                    "simulation_found_improvement"
                )



        # ==========================
        # FINAL DECISION
        # ==========================

        if score >= 1:

            decision = (
                "apply_corrective_action"
            )

            priority = "high"


        elif score >= 0.5:

            decision = (
                "optimize_system_state"
            )

            priority = "medium"


        else:

            decision = (
                "maintain_current_strategy"
            )

            priority = "low"



        return {


            "decision":
                decision,


            "priority":
                priority,


            "decision_score":
                round(
                    score,
                    3
                ),


            "reasons":
                reasons,


            "causal_basis":
                causal.get(
                    "cause",
                    "unknown"
                )

        }
