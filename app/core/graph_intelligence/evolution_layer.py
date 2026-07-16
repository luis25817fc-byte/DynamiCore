
"""
DynamiCore V6.11.0
Structural Evolution Intelligence Layer
"""


class EvolutionLayer:

    VERSION = "6.11.0"


    def analyze(
        self,
        previous,
        current
    ):

        previous = previous or {}

        current = current or {}


        changes = {}

        keys = set(previous) | set(current)


        for key in keys:

            old = previous.get(key)

            new = current.get(key)


            if old != new:

                changes[key] = {

                    "previous": old,

                    "current": new

                }


        change_count = len(changes)


        structural_pressure = 0


        for item in changes.values():

            old_value = item.get(
                "previous"
            )

            new_value = item.get(
                "current"
            )


            if isinstance(
                old_value,
                (int,float)
            ) and isinstance(
                new_value,
                (int,float)
            ):

                structural_pressure += abs(
                    new_value - old_value
                )

            else:

                structural_pressure += 1



        evolution_score = (
            change_count +
            structural_pressure
        )


        if evolution_score >= 10:

            transition_state = "HIGH_EVOLUTION"

        elif evolution_score >= 5:

            transition_state = "MODERATE_EVOLUTION"

        else:

            transition_state = "STABLE_EVOLUTION"



        return {

            "version":
                self.VERSION,

            "evolved":
                bool(changes),

            "changes":
                changes,

            "change_count":
                change_count,

            "structural_pressure":
                round(
                    structural_pressure,
                    4
                ),

            "evolution_score":
                round(
                    evolution_score,
                    4
                ),

            "transition_state":
                transition_state

        }
