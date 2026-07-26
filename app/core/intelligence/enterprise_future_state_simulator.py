from datetime import datetime, timezone
from uuid import uuid4
from copy import deepcopy


class EnterpriseFutureStateSimulator:
    """
    DLIS-066.2

    Enterprise Future State Simulator

    Genera múltiples proyecciones futuras
    a partir del estado actual del
    Enterprise Digital Twin.
    """

    VERSION = "1.0"


    def __init__(self):

        self.simulations = 0

        self.history = []


    def simulate(
        self,
        twin,
        projections=None
    ):

        if projections is None:

            projections = [

                {"name":"OPTIMISTIC","delta":0.05},

                {"name":"STABLE","delta":0.00},

                {"name":"CONSERVATIVE","delta":-0.05}

            ]


        current = deepcopy(
            twin.current_state
        )

        base = current.get(
            "cognitive_score",
            0.0
        )

        futures = []


        for projection in projections:

            score = round(
                max(
                    0.0,
                    min(
                        1.0,
                        base + projection["delta"]
                    )
                ),
                4
            )


            future = {

                "scenario_id":
                    str(uuid4()),

                "scenario":
                    projection["name"],

                "projected_score":
                    score,

                "timestamp":
                    datetime.now(
                        timezone.utc
                    ).isoformat()

            }

            futures.append(
                future
            )


        futures.sort(

            key=lambda x:
                x["projected_score"],

            reverse=True

        )


        result = {

            "simulation_id":
                str(uuid4()),

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "current_score":
                base,

            "best_future":
                futures[0],

            "future_states":
                futures,

            "version":
                self.VERSION

        }


        self.simulations += 1

        self.history.append(
            result
        )

        return result


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "simulations":
                self.simulations,

            "history_size":
                len(
                    self.history
                )

        }