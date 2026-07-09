
from .metrics.engine import MetricsEngine
from .predictive.forecast import ForecastEngine


class DynamiCoreEngine:


    def __init__(self):

        self.metrics = MetricsEngine()
        self.forecast = ForecastEngine()


    def analyze(self, system):

        if not system:
            return {
                "error": "empty input"
            }


        result = self.metrics.analyze(system)


        predictive = self.forecast.analyze(system)


        result["predictive"] = predictive

        result["system_size"] = len(system)


        return result
