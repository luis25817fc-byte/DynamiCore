
from datetime import datetime
from copy import deepcopy


class HistoricalEvolutionEngine:

    VERSION = "6.4.0"

    def __init__(self):
        self._history = []


    def record(
        self,
        signature,
        structural_intelligence,
        evolution,
        prediction,
        decision=None
    ):

        snapshot = {
            "id": len(self._history) + 1,
            "timestamp": datetime.utcnow().isoformat(),
            "signature": deepcopy(signature),
            "structural_intelligence": deepcopy(structural_intelligence),
            "evolution": deepcopy(evolution),
            "prediction": deepcopy(prediction),
            "decision": deepcopy(decision)
        }

        self._history.append(snapshot)

        return snapshot


    def latest(self):
        return deepcopy(self._history[-1]) if self._history else None


    def all(self):
        return deepcopy(self._history)


    def size(self):
        return len(self._history)
