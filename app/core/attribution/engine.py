
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



        total = sum(factors.values())


        contributions = {}


        for key,value in factors.items():

            contributions[key] = (
                value / total
                if total > 0
                else 0
            )



        dominant = max(
            contributions,
            key=contributions.get
        )



        return {


            "contributors": contributions,


            "dominant_factor": dominant,


            "confidence":
                contributions[dominant]


        }
