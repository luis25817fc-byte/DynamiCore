import numpy as np

class Entropy:
    def shannon(self, values):
        values = np.array(values, dtype=float)

        if values.sum() == 0:
            return 0.0

        p = values / values.sum()
        return -np.sum(p * np.log2(p + 1e-12))
