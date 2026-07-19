
class HistoryEngine:


    def __init__(self):

        self.history = []


    def add(self, state):

        self.history.append(state)


    def get(self):

        return self.history


    def latest(self):

        if not self.history:
            return None

        return self.history[-1]


    def size(self):

        return len(self.history)
