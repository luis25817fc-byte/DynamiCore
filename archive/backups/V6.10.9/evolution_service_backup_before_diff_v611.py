
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


        # salida limpia para snapshots

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


        previous = previous or {}

        current = current or {}


        changes = {}


        for key in set(previous) | set(current):


            if previous.get(key) != current.get(key):

                changes[key] = {

                    "previous":

                        previous.get(key),

                    "current":

                        current.get(key)

                }


        return {

            "version": self.version,

            "changed": bool(changes),

            "changes": changes

        }
