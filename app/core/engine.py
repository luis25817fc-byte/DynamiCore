
from .metrics.engine import MetricsEngine


class DynamiCoreEngine:


    def __init__(self):

        self.metrics = MetricsEngine()


    def analyze(self, system):

        if not system:
            return {
                "error": "empty input"
            }


        result = self.metrics.analyze(system)

        result["system_size"] = len(system)

        return result
