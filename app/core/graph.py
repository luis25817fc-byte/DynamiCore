
import numpy as np

class FunctionalGraph:
    def __init__(self, successor):
        self.successor = np.array(successor, dtype=np.int64)
        self.n = len(successor)

    def next_state(self, state):
        return int(self.successor[state])

def to_dict(self):
    return {
        "nodes": list(range(self.n)),
        "edges": [
            {
                "from": i,
                "to": int(self.successor[i])
            }
            for i in range(self.n)
        ]
    }

    def states(self):
        return range(self.n)

    def validate(self):
        if np.any(self.successor < 0):
            raise ValueError("[ERROR DYNAMICORE] No se permiten estados negativos.")
        if np.any(self.successor >= self.n):
            raise ValueError("[ERROR DYNAMICORE] Sucesor fuera de rango (sistema abierto).")
        return True
          
