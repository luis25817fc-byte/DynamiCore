
class ContextEngine:


    DOMAINS = [

        "industrial",
        "financial",
        "logistics",
        "medical",
        "cybersecurity",
        "research"

    ]


    def analyze(
        self,
        state,
        domain="general",
        metadata=None
    ):


        if domain not in self.DOMAINS:
            domain = "general"


        criticality = "low"


        if state.divergence > 1:
            criticality = "high"


        elif state.divergence > 0.5:
            criticality = "medium"



        stability = "stable"


        if state.dynamics < 0:
            stability = "degrading"


        if state.coherence < 0.3:
            stability = "unstable"



        return {


            "domain": domain,


            "criticality": criticality,


            "stability": stability,


            "state_summary": {


                "entropy": state.entropy,

                "coherence": state.coherence,

                "dynamics": state.dynamics,

                "potential": state.potential,

                "divergence": state.divergence

            },


            "metadata": metadata or {}

        }
