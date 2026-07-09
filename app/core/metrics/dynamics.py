
class DynamicsEngine:


    def analyze(self, coherence_history):

        if len(coherence_history) < 2:
            return {
                "first_derivative": 0,
                "second_derivative": 0,
                "regime_change": False,
                "critical_point": False,
                "trend": "stable"
            }


        first = coherence_history[-1] - coherence_history[-2]


        if len(coherence_history) >= 3:
            previous = coherence_history[-2] - coherence_history[-3]
            second = first - previous
        else:
            second = 0


        regime_change = abs(second) > 0.1

        critical_point = (
            abs(first) < 0.05 and 
            abs(second) > 0.2
        )


        if first > 0:
            trend = "increasing"
        elif first < 0:
            trend = "decreasing"
        else:
            trend = "stable"


        return {
            "first_derivative": first,
            "second_derivative": second,
            "regime_change": regime_change,
            "critical_point": critical_point,
            "trend": trend
        }
