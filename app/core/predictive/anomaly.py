
class AnomalyEngine:

    def analyze(self, system, history):

        if not isinstance(system, list):
            return {
                "anomaly": False,
                "score": 0,
                "reason": "invalid_type"
            }

        if len(system) == 0:
            return {
                "anomaly": False,
                "score": 0,
                "reason": "empty_system"
            }

        current_avg = sum(system) / len(system)

        if not history:
            return {
                "anomaly": False,
                "score": 0,
                "reason": "no_history"
            }

        previous = history[-1]

        if not isinstance(previous, list):
            return {
                "anomaly": False,
                "score": 0,
                "reason": "invalid_history"
            }

        if len(previous) == 0:
            return {
                "anomaly": False,
                "score": 0,
                "reason": "empty_history"
            }

        previous_avg = sum(previous) / len(previous)

        delta = abs(current_avg - previous_avg)

        score = delta / (abs(previous_avg) + 1e-9)

        return {
            "anomaly": score > 0.25,
            "score": round(score,6),
            "delta": round(delta,6)
        }
