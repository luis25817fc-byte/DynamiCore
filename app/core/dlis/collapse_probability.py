
import math


class CollapseProbabilityEngine:

    VERSION = "DLIS-005"


    def compute(
        self,
        potential
    ):

        probability = (
            1 -
            math.exp(-potential)
        )

        return {

            "version":
                self.VERSION,

            "potential":
                potential,

            "collapse_probability":
                probability

        }
