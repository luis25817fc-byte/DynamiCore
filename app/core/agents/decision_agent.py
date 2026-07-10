
from .base import BaseAgent



class DecisionAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "decision_agent"
        )


    def run(
        self,
        data
    ):


        return {

            "agent":
                self.name,

            "decision":
                "optimize_system_state"

        }
