
from dataclasses import dataclass
from math import isclose


@dataclass
class InvariantReport:

    version: str
    invariant_entropy: bool
    invariant_resilience: bool
    invariant_divergence: bool
    invariant_energy: bool
    invariant_score: float
    transition_class: str



class InvariantEngine:

    VERSION = "7.3"

    TOLERANCE = 1e-6


    def _get(self, obj, key, default=0.0):

        if isinstance(obj, dict):
            return obj.get(key, default)

        return getattr(
            obj,
            key,
            default
        )


    def compare_values(self, a, b):

        return isclose(
            a,
            b,
            rel_tol=self.TOLERANCE,
            abs_tol=self.TOLERANCE
        )


    def compare(self, previous, current):

        entropy_ok = self.compare_values(
            self._get(previous, "entropy"),
            self._get(current, "entropy")
        )

        resilience_ok = self.compare_values(
            self._get(previous, "resilience"),
            self._get(current, "resilience")
        )

        divergence_ok = self.compare_values(
            self._get(previous, "divergence"),
            self._get(current, "divergence")
        )

        energy_ok = self.compare_values(
            self._get(previous, "phi"),
            self._get(current, "phi")
        )


        score = (
            int(entropy_ok)
            +
            int(resilience_ok)
            +
            int(divergence_ok)
            +
            int(energy_ok)
        ) / 4


        if score == 1:
            transition = "STRUCTURAL_INVARIANT"
        elif score >= 0.75:
            transition = "STABLE_VARIATION"
        elif score >= 0.5:
            transition = "STRUCTURAL_SHIFT"
        elif score >= 0.25:
            transition = "MAJOR_TRANSITION"
        else:
            transition = "CRITICAL_RECONFIGURATION"


        return InvariantReport(

            version=self.VERSION,

            invariant_entropy=entropy_ok,

            invariant_resilience=resilience_ok,

            invariant_divergence=divergence_ok,

            invariant_energy=energy_ok,

            invariant_score=score,

            transition_class=transition
        )


    def status(self):

        return {
            "version": self.VERSION,
            "module": "InvariantEngine",
            "status": "ONLINE"
        }
