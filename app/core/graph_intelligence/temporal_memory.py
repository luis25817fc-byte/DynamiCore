
class TemporalGraphMemory:

    VERSION="6.2.5"

    def __init__(self):
        self.history=[]

    def store(self,signature):

        self.history.append(signature)

        return{
            "version":self.VERSION,
            "stored":len(self.history)
        }

    def latest(self,n=5):

        return{
            "version":self.VERSION,
            "history":self.history[-n:]
        }
