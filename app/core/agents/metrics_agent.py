
from .base import BaseAgent


class MetricsAgent(BaseAgent):

    def __init__(self):
        super().__init__("metrics_agent")


    def run(self, data):

        return {
            "agent": self.name,
            "metrics": data.get("metrics", {})
        }
