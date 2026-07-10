
from .metrics.engine import MetricsEngine

from .predictive.forecast import ForecastEngine
from .predictive.risk import RiskEngine
from .predictive.regime import RegimeEngine
from .predictive.anomaly import AnomalyEngine

from .state.snapshot import SnapshotEngine

from .kernel.state_vector import StateVector

from .agents.orchestrator import AgentOrchestrator



class DynamiCoreEngine:


    def __init__(self):

        self.metrics = MetricsEngine()

        self.forecast = ForecastEngine()
        self.risk = RiskEngine()
        self.regime = RegimeEngine()
        self.anomaly = AnomalyEngine()

        self.snapshots = SnapshotEngine()

        self.agents = AgentOrchestrator()



    def analyze(self, system):


        if not system:

            return {
                "error":"empty input"
            }



        result = self.metrics.analyze(
            system
        )



        predictive = self.forecast.analyze(
            system
        )

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



        history = []

        for s in self.snapshots.all():

            if not isinstance(s,dict):
                continue


            if "analysis" in s:

                state = s["analysis"].get(
                    "system",
                    []
                )

            else:

                state = s.get(
                    "system",
                    []
                )


            if state:

                history.append(
                    state
                )



        result["system"] = system



        anomaly = self.anomaly.analyze(
            system,
            history
        )


        result["anomaly"] = anomaly



        result["system_size"] = len(system)



        # ==========================
        # STATE VECTOR
        # ==========================

        state_vector = StateVector(

            entropy=result["H(k)"]["shannon"],

            coherence=result["R(k)"]["R(k)"],

            dynamics=result["ΔR(k)"]["first_derivative"],

            potential=result["Ψ(k)"]["Ψ(k)"],

            divergence=result["D(k)"]["D(k)"]

        )


        result["state_vector"] = state_vector.to_dict()



        # ==========================
        # AGENT INTELLIGENCE
        # ==========================

        result["agents"] = self.agents.execute(
            result
        )



        self.snapshots.save(
            result
        )



        return result
