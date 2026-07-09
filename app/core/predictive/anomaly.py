
class AnomalyEngine:


    def analyze(self, system, history):

        if not history:
            return {
                "anomaly": False,
                "deviation": 0,
                "severity": "unknown"
            }


        previous = history[-1]


        current_avg = sum(system) / len(system)

        previous_avg = sum(previous) / len(previous)


        deviation = abs(
            current_avg - previous_avg
        )


        if deviation >= 1:
            severity = "high"
            anomaly = True

        elif deviation >= 0.5:
            severity = "medium"
            anomaly = True

        else:
            severity = "low"
            anomaly = False


        return {
            "anomaly": anomaly,
            "deviation": round(deviation, 4),
            "severity": severity
        }
