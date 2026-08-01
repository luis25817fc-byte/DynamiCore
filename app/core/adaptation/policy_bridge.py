from .policy_evolution import PolicyEvolutionEngine


class PolicyBridge:

    VERSION = "6.1"


    def __init__(self, evolution=None):

        self.evolution = (
            evolution
            if evolution is not None
            else PolicyEvolutionEngine()
        )


    def update(self, policy, feedback):

        if isinstance(policy, dict):
            policy = policy.get(
                "strategy",
                "unknown"
            )

        self.evolution.record(
            policy,
            feedback.get(
                "outcome",
                "unknown"
            )
        )

        return self.evolution.best_policy()
