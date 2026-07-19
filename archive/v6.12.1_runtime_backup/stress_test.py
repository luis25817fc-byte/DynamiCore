import time
import numpy as np

from dynamicore.core.analyzer import DynamiCore


def stress_test(sizes, runs_per_size=15):

    results = {}

    for n in sizes:

        print(f"\n🔬 Testing size: {n}")

        times = []

        for _ in range(runs_per_size):

            system = np.random.permutation(n)

            start = time.perf_counter()

            DynamiCore(system.tolist()).analyze()

            end = time.perf_counter()

            times.append((end-start)*1000)

        results[n] = {
            "size": n,
            "avg_ms": float(np.mean(times)),
            "p95_ms": float(np.percentile(times,95)),
            "max_ms": float(np.max(times)),
            "std_ms": float(np.std(times))
        }

    return results
