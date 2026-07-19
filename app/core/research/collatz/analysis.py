
class CollatzAnalyzer:


    def analyze(self, trajectory):

        if not trajectory:
            return {
                "error": "empty trajectory"
            }


        changes = []

        for i in range(len(trajectory)-1):
            changes.append(
                trajectory[i+1] - trajectory[i]
            )


        max_value = max(trajectory)
        final_state = trajectory[-1]


        return {

            "initial_state": trajectory[0],

            "final_state": final_state,

            "steps": len(trajectory),

            "max_energy": max_value,

            "growth_peak": max_value / trajectory[0],

            "average_transition":
                sum(changes) / len(changes),

            "expansion":
                max_value > trajectory[0],

            "converged":
                final_state == 1
        }
