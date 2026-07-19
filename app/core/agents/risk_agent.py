
from .base import BaseAgent



class RiskAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "risk_agent"
        )


    def run(
        self,
        data
    ):

        risk = data.get(
            "risk",
            {}
        )


        return {

            "agent":
                self.name,

            "risk":
                risk

        }
