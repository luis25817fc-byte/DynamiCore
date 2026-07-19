
import math
from collections import Counter


class EntropyEngine:

    def shannon(self, system):

        if not system:
            return 0.0

        counts = Counter(system)
        total = len(system)

        return sum(
            -(count/total) * math.log2(count/total)
            for count in counts.values()
        )


    def normalized(self, system):

        if len(system) <= 1:
            return 0.0

        return self.shannon(system) / math.log2(len(system))


    def entropy_rate(self, history):

        if len(history) < 2:
            return 0.0

        return abs(history[-1] - history[-2])
