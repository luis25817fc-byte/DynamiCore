
class PolicyBridge:


    def __init__(self, evolution):

        self.evolution = evolution



    def update(

        self,

        policy,

        feedback

    ):


        self.evolution.record(

            policy,

            feedback.get(
                "outcome",
                "unknown"
            )

        )


        return self.evolution.best_policy()
