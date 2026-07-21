
from datetime import datetime, timezone


class CognitiveMemoryLayer:

    VERSION = "DLIS-028"


    def __init__(self, trace_store=None):

        self.trace_store = trace_store


    def load_history(self):

        if not self.trace_store:
            return []

        return self.trace_store.load()


    def count_decisions(self):

        history = self.load_history()

        return {

            "version": self.VERSION,

            "total_traces": len(history)

        }


    def find_by_objective(
        self,
        objective
    ):

        history = self.load_history()

        matches = []

        for trace in history:

            current = (
                trace
                .get("objective", {})
                .get("objective")
            )

            if current == objective:
                matches.append(trace)


        return {

            "version": self.VERSION,

            "objective": objective,

            "matches": len(matches),

            "traces": matches

        }
