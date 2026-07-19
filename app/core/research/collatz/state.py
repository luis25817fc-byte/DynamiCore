
from app.core.kernel import StateVector


class CollatzStateBuilder:

    def build(self, analysis):

        return StateVector(

            entropy=min(
                analysis["steps"] / 100,
                10
            ),

            coherence=(
                1.0 if analysis["converged"]
                else 0.0
            ),

            dynamics=analysis["average_transition"],

            potential=analysis["max_energy"],

            divergence=analysis["growth_peak"]
        )
