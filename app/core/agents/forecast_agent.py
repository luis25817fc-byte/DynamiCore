
from .base import BaseAgent



class ForecastAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "forecast_agent"
        )


    def run(
        self,
        data
    ):

        return {

            "agent":
                self.name,

            "forecast":
                data.get(
                    "forecast",
                    {}
                )

        }
