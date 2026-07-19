
from .metrics_agent import MetricsAgent
from .risk_agent import RiskAgent
from .forecast_agent import ForecastAgent
from .decision_agent import DecisionAgent



class AgentOrchestrator:


    def __init__(self):

        self.agents = [

            MetricsAgent(),

            RiskAgent(),

            ForecastAgent(),

            DecisionAgent()

        ]



    def execute(
        self,
        data
    ):


        results = {}


        for agent in self.agents:

            results[
                agent.name
            ] = agent.run(
                data
            )


        return results
