
from .metrics.engine import MetricsEngine

from .predictive.forecast import ForecastEngine
from .predictive.risk import RiskEngine
from .predictive.regime import RegimeEngine
from .predictive.anomaly import AnomalyEngine

from .state.snapshot import SnapshotEngine


class DynamiCoreEngine:


    def __init__(self):

        self.metrics = MetricsEngine()

        self.forecast = ForecastEngine()
        self.risk = RiskEngine()
        self.regime = RegimeEngine()
        self.anomaly = AnomalyEngine()

        self.snapshots = SnapshotEngine()



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


        regime = self.regime.analyze(
            predictive,
            risk
        )
        result["regime_analysis"] = regime


        history = [
            s["analysis"].get("system", [])
            for s in self.snapshots.all()
        ]


        result["system"] = system


        anomaly = self.anomaly.analyze(
            system,
            history
        )

        result["anomaly"] = anomaly


        result["system_size"] = len(system)


        self.snapshots.save(result)


        return result
