
class ForecastEngine:

    def analyze(self, history):

        if len(history) < 3:
            return {
                "error": "insufficient_history"
            }

        n = len(history)

        # tendencia simple
        trend = history[-1] - history[0]

        # velocidad de cambio
        velocity = (
            history[-1] - history[-2]
        )

        # aceleración
        acceleration = (
            history[-1]
            - 2 * history[-2]
            + history[-3]
        )

        # predicción siguiente estado
        next_state = (
            history[-1]
            + velocity
            + acceleration
        )

        if acceleration > 0:
            regime = "expanding"
        elif acceleration < 0:
            regime = "contracting"
        else:
            regime = "stable"


        return {
            "trend": trend,
            "velocity": velocity,
            "acceleration": acceleration,
            "next_state": next_state,
            "regime": regime
        }
