
class DivergenceEngine:


    def analyze(self, current, historical, attractor):

        structural_divergence = abs(current - historical)

        historical_distance = abs(historical)
        
        attractor_distance = abs(current - attractor)


        anomaly = (
            structural_divergence > 1 or
            attractor_distance > 1
        )


        risk = min(
            1.0,
            (structural_divergence +
             attractor_distance) / 5
        )


        D = (
            structural_divergence +
            historical_distance +
            attractor_distance +
            risk
        ) / 4


        return {
            "structural_divergence": structural_divergence,
            "historical_distance": historical_distance,
            "attractor_distance": attractor_distance,
            "anomaly": anomaly,
            "risk": risk,
            "D(k)": D
        }
