
class EvolutionMetrics:

    VERSION = "6.5.1"

    def calculate(self, diff, transition):

        growth = diff.get(
            "growth",
            0
        )

        return {
            "version": self.VERSION,
            "growth": growth,
            "transition": transition,
            "evolution_pressure":
                abs(growth)
        }
