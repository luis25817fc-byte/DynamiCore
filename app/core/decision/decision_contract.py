
"""
DynamiCore V6.10.0
Decision Contract
"""


class DecisionContract:

    VERSION = "6.10.0"

    def build(
        self,
        decision,
        priority,
        confidence,
        risk,
        reason,
        next_actions=None
    ):

        return {

            "version": self.VERSION,

            "decision": decision,

            "priority": priority,

            "confidence": confidence,

            "risk": risk,

            "reason": reason,

            "next_actions": (
                next_actions
                or []
            )
        }
