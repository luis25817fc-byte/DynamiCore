
class CollatzEngine:


    def generate(self, n, max_steps=10000):

        trajectory = [n]
        seen = set()


        for _ in range(max_steps):

            if n == 1:
                break


            if n in seen:
                return {
                    "initial": trajectory[0],
                    "trajectory": trajectory,
                    "steps": len(trajectory),
                    "cycle_detected": True
                }


            seen.add(n)


            if n % 2 == 0:
                n = n // 2
            else:
                n = 3*n + 1


            trajectory.append(n)


        return {
            "initial": trajectory[0],
            "trajectory": trajectory,
            "steps": len(trajectory),
            "cycle_detected": False
        }
