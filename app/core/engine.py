
from .metrics.engine import MetricsEngine

from .predictive.forecast import ForecastEngine
from .predictive.risk import RiskEngine
from .predictive.regime import RegimeEngine
from .predictive.anomaly import AnomalyEngine

from .state.snapshot import SnapshotEngine

from .kernel.state_vector import StateVector

from .agents.orchestrator import AgentOrchestrator

from .state.evolution import EvolutionEngine
from .state.transition import StateTransitionEngine

from .twin.engine import TwinEngine

from .simulation.engine import ScenarioEngine

from .attribution.engine import AttributionEngine
from .causal.engine import CausalEngine
from .decision.engine import DecisionEngine



class DynamiCoreEngine:


    def __init__(self):

        self.metrics = MetricsEngine()

        self.forecast = ForecastEngine()
        self.risk = RiskEngine()
        self.regime = RegimeEngine()
        self.anomaly = AnomalyEngine()

        self.snapshots = SnapshotEngine()

        self.agents = AgentOrchestrator()

        self.evolution = EvolutionEngine()

        self.transition = StateTransitionEngine()

        self.twin = TwinEngine()

        self.scenario = ScenarioEngine()

        self.attribution = AttributionEngine()

        self.causal = CausalEngine()

        self.decision = DecisionEngine()



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



        result["regime_analysis"] = self.regime.analyze(
            predictive,
            risk
        )



        history=[]

        for s in self.snapshots.all():

            if not isinstance(s,dict):
                continue


            if "analysis" in s:

                old = s["analysis"].get(
                    "system",
                    []
                )

            else:

                old = s.get(
                    "system",
                    []
                )


            if old:
                history.append(old)



        result["system"] = system



        result["anomaly"] = self.anomaly.analyze(
            system,
            history
        )



        state_vector = StateVector(

            entropy=result["H(k)"]["shannon"],

            coherence=result["R(k)"]["R(k)"],

            dynamics=result["ΔR(k)"]["first_derivative"],

            potential=result["Ψ(k)"]["Ψ(k)"],

            divergence=result["D(k)"]["D(k)"]

        )


        result["state_vector"] = state_vector.to_dict()



        # ==========================
        # ATTRIBUTION INTELLIGENCE
        # ==========================

        attribution = self.attribution.analyze(
            state_vector
        )

        result["attribution"] = attribution



        # Adaptador causal

        causal_input = attribution.copy()


        mapping = {

            "coherence_change":
                "coherence_drop",

            "divergence_change":
                "divergence_growth",

            "entropy_change":
                "entropy_growth"

        }


        factor = attribution["dominant_factor"]


        causal_input["dominant_factor"] = mapping.get(
            factor,
            factor
        )


        causal = self.causal.analyze(
            causal_input
        )


        result["causal"] = causal



        decision = self.decision.decide(

            state_vector,

            {},

            causal

        )


        result["decision"] = decision



        # ==========================
        # EVOLUTION INTELLIGENCE
        # ==========================

        snapshots = self.snapshots.all()

        previous = None

        if len(snapshots) > 0:
            previous = snapshots[-1]


        current_snapshot = {
            "analysis": result
        }


        result["evolution"] = self.evolution.compare(
            previous,
            current_snapshot
        )



        # ==========================
        # DIGITAL TWIN STATUS
        # ==========================

        result["twin_state"] = {

            "available":
                self.twin.list()

        }



        result["agents"] = self.agents.execute(
            result
        )



        result["system_size"] = len(system)



        self.snapshots.save(
            result
        )


        return result
