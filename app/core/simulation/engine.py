
from .scenario import Scenario



class ScenarioEngine:


    def simulate(
        self,
        state,
        changes
    ):


        scenario = Scenario(
            "custom_scenario",
            changes
        )


        result = scenario.apply(
            state
        )


        before_risk = (
            state.divergence
            +
            abs(state.dynamics)
        )



        after_risk = (
            result["divergence"]
            +
            abs(result["dynamics"])
        )



        improvement = (
            before_risk
            -
            after_risk
        )



        return {


            "scenario":
                scenario.name,


            "before":{

                "risk":
                    before_risk

            },


            "after":{

                "risk":
                    after_risk

            },


            "impact":
                improvement,


            "state":
                result

        }
