
class AttributionEngine:


    def analyze(self, state, previous=None):

        factors = {}


        if previous:

            factors["entropy_change"] = abs(
                state.entropy -
                previous.entropy
            )

            factors["coherence_change"] = abs(
                state.coherence -
                previous.coherence
            )

            factors["dynamics_change"] = abs(
                state.dynamics -
                previous.dynamics
            )

            factors["potential_change"] = abs(
                state.potential -
                previous.potential
            )

            factors["divergence_change"] = abs(
                state.divergence -
                previous.divergence
            )

        else:

            factors = {

                "entropy_change":
                    abs(state.entropy),

                "coherence_change":
                    abs(1-state.coherence),

                "dynamics_change":
                    abs(state.dynamics),

                "potential_change":
                    abs(state.potential),

                "divergence_change":
                    abs(state.divergence)

            }


        total = sum(
            factors.values()
        )


        contributions = {}

        for key,value in factors.items():

            contributions[key] = (
                value / total
                if total > 0
                else 0
            )


        ranking = sorted(
            contributions.items(),
            key=lambda x: x[1],
            reverse=True
        )


        dominant = ranking[0][0]


        confidence = ranking[0][1]


        if confidence > 0.7:

            severity = "dominant"

        elif confidence > 0.4:

            severity = "moderate"

        else:

            severity = "distributed"


        return {

            "contributors":
                contributions,

            "ranking":
                ranking,

            "dominant_factor":
                dominant,

            "confidence":
                confidence,

            "severity":
                severity

        }
