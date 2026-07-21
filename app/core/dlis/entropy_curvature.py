
class EntropyCurvatureEngine:

    VERSION = "DLIS-007"

    EPSILON = 1e-9

    def compute(
        self,
        delta_potential,
        structural_energy
    ):

        curvature = (
            delta_potential /
            (
                structural_energy +
                self.EPSILON
            )
        )

        if curvature > 0:
            regime = "ACCELERATING"

        elif curvature < 0:
            regime = "DECELERATING"

        else:
            regime = "STABLE"

        return {

            "version": self.VERSION,

            "delta_potential": delta_potential,

            "structural_energy": structural_energy,

            "entropy_curvature": curvature,

            "regime": regime

        }
