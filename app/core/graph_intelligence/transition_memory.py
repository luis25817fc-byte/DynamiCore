
class TransitionMemory:

    VERSION = "6.5.0"

    def __init__(self):
        self.transitions = []


    def record(self, before, after, diff):

        item = {
            "before": before,
            "after": after,
            "diff": diff
        }

        self.transitions.append(item)

        return item


    def history(self):

        return self.transitions
