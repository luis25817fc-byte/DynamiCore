
from collections import Counter
import math


class DynamiCoreEngine:

    VERSION = "CORE-018"

    def __init__(self):
        pass


    def analyze(self, system):

        if not system:
            return {
                "state_vector": {
                    "entropy": 0,
                    "coherence": 0,
                    "potential": 0,
                    "divergence": 0,
                    "dynamics": 0
                }
            }


        total = len(system)

        counts = Counter(system)


        entropy = sum(
            -(count / total) *
            math.log2(count / total)
            for count in counts.values()
        )


        mean = sum(system) / total


        variance = sum(
            (x - mean) ** 2
            for x in system
        ) / total


        coherence = 1 / (1 + variance)


        potential = entropy + coherence


        divergence = abs(
            entropy - coherence
        )


        dynamics = (
            coherence - entropy
        )


        return {

            "state_vector": {

                "entropy": entropy,

                "coherence": coherence,

                "potential": potential,

                "divergence": divergence,

                "dynamics": dynamics

            },

            "system": system

        }
