
import sys
from pathlib import Path
import time
import numpy as np

# ============================================================
# DYNAMICORE V7 ENTERPRISE PATH CONFIGURATION
# ============================================================

ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(
    0,
    str(ROOT)
)

# ============================================================
# DYNAMICORE CORE IMPORT
# ============================================================

try:
    from app.core.analyzer import DynamiCore
except ImportError:
    try:
        from app.core.engine import DynamiCoreEngine as DynamiCore
    except ImportError as error:
        raise ImportError(
            f"""
DynamiCore Core import failed.

Expected:
app.core.analyzer.DynamiCore
or
app.core.engine.DynamiCoreEngine

Original error:
{error}
"""
        )


# ============================================================
# STRESS TEST ENGINE
# ============================================================

def stress_test(sizes, runs_per_size=15):

    results = {}

    for n in sizes:

        print(f"\n🔬 Testing size: {n}")

        times = []

        for _ in range(runs_per_size):

            system = np.random.permutation(n)

            start = time.perf_counter()

            engine = DynamiCore()

            try:
                engine.analyze(system)

            except TypeError:
                try:
                    engine.analyze(
                        list(system)
                    )
                except Exception as e:
                    print(
                        "Analysis warning:",
                        e
                    )

            elapsed = time.perf_counter() - start

            times.append(elapsed)


        results[n] = {
            "average_seconds": float(
                np.mean(times)
            ),
            "min_seconds": float(
                np.min(times)
            ),
            "max_seconds": float(
                np.max(times)
            )
        }


        print(
            f"Average: {results[n]['average_seconds']:.6f}s"
        )


    return results



# ============================================================
# EXECUTION
# ============================================================

if __name__ == "__main__":

    print("=" * 100)
    print("DYNAMICORE V7 ENTERPRISE STRESS TEST")
    print("=" * 100)

    sizes = [
        32,
        64,
        128,
        256,
        512
    ]

    report = stress_test(
        sizes
    )

    print("\n")
    print("=" * 100)
    print("FINAL BENCHMARK REPORT")
    print("=" * 100)

    for size, data in report.items():

        print(
            f"""
SIZE: {size}
AVG: {data['average_seconds']:.6f}s
MIN: {data['min_seconds']:.6f}s
MAX: {data['max_seconds']:.6f}s
"""
        )
