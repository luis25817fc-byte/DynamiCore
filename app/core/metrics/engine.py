
from .entropy import EntropyEngine
from .coherence import CoherenceEngine
from .dynamics import DynamicsEngine
from .potential import PotentialEngine
from .divergence import DivergenceEngine


class MetricsEngine:


    def __init__(self):

        self.entropy = EntropyEngine()
        self.coherence = CoherenceEngine()
        self.dynamics = DynamicsEngine()
        self.potential = PotentialEngine()
        self.divergence = DivergenceEngine()


    def analyze(self, system):

        H = {
            "shannon": self.entropy.shannon(system),
            "normalized": self.entropy.normalized(system),
            "entropy_rate": self.entropy.entropy_rate(system)
        }


        R = self.coherence.compute(system)


        history = [
            0.2,
            0.4,
            R["R(k)"]
        ]

        delta_R = self.dynamics.analyze(history)


        PSI = self.potential.analyze(system)


        D = self.divergence.analyze(
            R["R(k)"],
            0.5,
            0
        )


        alert = "normal"

        if D["anomaly"]:
            alert = "warning"


        regime = "stable"

        if delta_R["regime_change"]:
            regime = "unstable"


        return {
            "H(k)": H,
            "R(k)": R,
            "ΔR(k)": delta_R,
            "Ψ(k)": PSI,
            "D(k)": D,
            "alert_level": alert,
            "regime": regime
        }


# Alias compatible
MetricsEngine.analyse = MetricsEngine.analyze
