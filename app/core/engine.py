
from .metrics.engine import MetricsEngine
from .predictive.forecast import ForecastEngine
from .predictive.risk import RiskEngine


class DynamiCoreEngine:


    def __init__(self):

        self.metrics = MetricsEngine()
        self.forecast = ForecastEngine()
        self.risk = RiskEngine()


    def analyze(self, system):

        if not system:
            return {
                "error": "empty input"
            }


        result = self.metrics.analyze(system)


        predictive = self.forecast.analyze(system)

        result["predictive"] = predictive


        risk = self.risk.analyze(
            predictive,
            result
        )

        result["risk"] = risk


        result["system_size"] = len(system)


        return result
