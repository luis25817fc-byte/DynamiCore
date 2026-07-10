
class Scenario:


    def __init__(
        self,
        name,
        changes
    ):

        self.name = name
        self.changes = changes



    def apply(
        self,
        state
    ):


        values = {


            "entropy":
                state.entropy,


            "coherence":
                state.coherence,


            "dynamics":
                state.dynamics,


            "potential":
                state.potential,


            "divergence":
                state.divergence

        }



        for key, value in self.changes.items():

            if key in values:

                values[key] += value



        return values
