
class DecisionEngine:


    def decide(
        self,
        state,
        context,
        causal
    ):


        priority = "low"


        if state.divergence > 1:
            priority = "high"

        elif state.divergence > 0.5:
            priority = "medium"



        actions = []



        if causal.get("causal_found"):


            cause = causal["cause"]


            if cause == "coherence_drop":

                actions.append(
                    "increase_system_stability"
                )


            elif cause == "divergence_growth":

                actions.append(
                    "reduce_structural_divergence"
                )


            elif cause == "entropy_growth":

                actions.append(
                    "reduce_system_complexity"
                )


        else:

            actions.append(
                "collect_more_information"
            )



        impact = 0.0


        if priority == "high":

            impact = 0.8

        elif priority == "medium":

            impact = 0.5

        else:

            impact = 0.2



        return {


            "decision":
                actions[0],


            "priority":
                priority,


            "actions":
                actions,


            "reason":
                causal.get(
                    "cause",
                    "unknown"
                ),


            "expected_impact":
                impact,


            "domain":
                context.get(
                    "domain",
                    "general"
                )

        }
