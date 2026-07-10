
from .policy_evolution import PolicyEvolutionEngine


class EvolutionAdapter:


    def __init__(self):

        self.version = "6.1"

        self.evolution = PolicyEvolutionEngine()



    def process(

        self,

        policy,

        feedback

    ):


        stored = self.evolution.record(

            policy,

            feedback.get(
                "outcome",
                "unknown"
            )

        )


        recommendation = self.evolution.best_policy()


        return {

            "version": self.version,

            "stored": stored,

            "recommendation": recommendation

        }
