
from .model import DigitalTwin



class TwinEngine:


    def __init__(self):

        self.twins = {}



    def create(
        self,
        name,
        state
    ):


        twin = DigitalTwin(
            name,
            state
        )


        self.twins[name] = twin


        return twin.snapshot()



    def update(
        self,
        name,
        state
    ):


        twin = self.twins.get(
            name
        )


        if not twin:

            return {

                "error":
                "twin_not_found"

            }


        twin.update(
            state
        )


        return twin.snapshot()



    def get(
        self,
        name
    ):


        twin = self.twins.get(
            name
        )


        if not twin:

            return None


        return twin.snapshot()



    def list(self):

        return list(
            self.twins.keys()
        )
