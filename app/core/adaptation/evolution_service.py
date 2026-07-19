
from .evolution_adapter import EvolutionAdapter
from .evolution_diff import EvolutionDiffEngine


class EvolutionService:


    def __init__(self):

        self.version = "6.1"

        self.adapter = EvolutionAdapter()

        self.diff_engine = EvolutionDiffEngine()



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

            "policy": str(policy),

            "outcome": str(

                feedback.get(

                    "outcome",

                    "unknown"

                )

            ),

            "stored": {

                "uses":

                    result.get(

                        "stored",

                        {}

                    ).get(

                        "uses",

                        0

                    ),

                "success":

                    result.get(

                        "stored",

                        {}

                    ).get(

                        "success",

                        0

                    ),

                "failed":

                    result.get(

                        "stored",

                        {}

                    ).get(

                        "failed",

                        0

                    )

            }

        }



    def recommendation(self):


        best = self.adapter.evolution.best_policy()


        return {

            "policy":

                best.get(

                    "policy",

                    "observe"

                ),

            "confidence":

                best.get(

                    "confidence",

                    0

                )

        }



    def compare(

        self,

        previous,

        current

    ):


        return self.diff_engine.compare(

            previous,

            current

        )
