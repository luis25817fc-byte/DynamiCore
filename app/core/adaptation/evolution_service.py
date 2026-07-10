
from .evolution_adapter import EvolutionAdapter


class EvolutionService:


    def __init__(self):

        self.version = "6.1"

        self.adapter = EvolutionAdapter()



    def evaluate(

        self,

        policy,

        feedback

    ):


        result = self.adapter.process(

            policy,

            feedback

        )


        return {

            "version": self.version,

            "policy": policy,

            "feedback":

                feedback,

            "evolution":

                result

        }



    def recommendation(self):


        return self.adapter.evolution.best_policy()
