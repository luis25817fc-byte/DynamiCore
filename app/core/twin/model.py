
from datetime import datetime



class DigitalTwin:


    def __init__(
        self,
        name,
        state
    ):

        self.name = name

        self.state = state

        self.history = []


        self.record()



    def update(
        self,
        state
    ):

        self.state = state

        self.record()



    def record(self):

        self.history.append({

            "timestamp":
                datetime.utcnow().isoformat(),

            "state":
                self.state.to_dict()

        })



    def snapshot(self):

        return {

            "name":
                self.name,


            "current_state":
                self.state.to_dict(),


            "history_size":
                len(self.history)

        }
