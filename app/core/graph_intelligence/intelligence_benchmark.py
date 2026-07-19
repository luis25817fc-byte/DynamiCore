
import time


class IntelligenceBenchmark:

    VERSION = "6.5.8"

    def run(
        self,
        engine,
        previous,
        current,
        runs=5
    ):

        outputs = []
        times = []

        for _ in range(runs):

            start = time.time()

            result = engine.run(
                previous,
                current
            )

            end = time.time()

            outputs.append(
                result["dynamic_state"]
            )

            times.append(
                end - start
            )

        stable = len(
            set(
                str(x)
                for x in outputs
            )
        ) == 1

        avg_time = (
            sum(times)
            /
            len(times)
        )

        return {
            "version": self.VERSION,
            "benchmark": (
                "PASSED"
                if stable
                else "FAILED"
            ),
            "runs": runs,
            "average_execution_time": avg_time,
            "state_stability": (
                "HIGH"
                if stable
                else "LOW"
            ),
            "consistency_score": (
                1.0
                if stable
                else 0.0
            )
        }
