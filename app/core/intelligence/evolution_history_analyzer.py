
from statistics import mean


class EvolutionHistoryAnalyzerV751:

    VERSION = "7.5.1"


    def analyze(self, states, transitions):

        if not states:

            return {

                "version": self.VERSION,

                "status": "EMPTY"

            }


        entropies = [

            s.get("entropy",0)

            for s in states

        ]


        health = [

            s.get("structural_health",0)

            for s in states

        ]


        risks = [

            s.get("transition_risk",0)

            for s in states

        ]


        entropy_delta = (

            entropies[-1] - entropies[0]

            if len(entropies) > 1

            else 0.0

        )


        health_delta = (

            health[-1] - health[0]

            if len(health) > 1

            else 0.0

        )


        if entropy_delta > 0:

            entropy_trend = "INCREASING"

        elif entropy_delta < 0:

            entropy_trend = "DECREASING"

        else:

            entropy_trend = "STABLE"


        if health_delta > 0:

            health_trend = "RECOVERING"

        elif health_delta < 0:

            health_trend = "DEGRADING"

        else:

            health_trend = "STABLE"


        return {

            "version": self.VERSION,

            "states": len(states),

            "transitions": len(transitions),

            "entropy_mean": round(

                mean(entropies),

                6

            ),

            "health_mean": round(

                mean(health),

                6

            ),

            "risk_mean": round(

                mean(risks),

                6

            ),

            "entropy_delta": round(

                entropy_delta,

                6

            ),

            "health_delta": round(

                health_delta,

                6

            ),

            "entropy_trend": entropy_trend,

            "health_trend": health_trend,

            "status": "ONLINE"

        }
