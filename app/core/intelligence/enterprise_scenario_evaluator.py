from datetime import datetime, timezone



class EnterpriseScenarioEvaluator:
    """
    DLIS-061.1

    Scenario Evaluation Layer

    Evalúa futuros simulados
    y selecciona el escenario óptimo.
    """

    VERSION = "1.0"



    def __init__(self):

        self.evaluations = 0

        self.history = []



    def evaluate(
        self,
        simulation
    ):


        scenarios = simulation.get(
            "scenarios",
            []
        )


        ranked = sorted(

            scenarios,

            key=lambda x:
                x.get(
                    "projected_score",
                    0
                ),

            reverse=True

        )



        best = ranked[0] if ranked else None



        result = {

            "evaluation_id":
                self.evaluations + 1,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "simulation_id":
                simulation.get(
                    "simulation_id"
                ),

            "best_scenario":
                best,

            "ranking":
                ranked,

            "version":
                self.VERSION

        }



        self.evaluations += 1


        self.history.append(
            result
        )


        return result



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "evaluations":
                self.evaluations,

            "history_size":
                len(self.history)

        }