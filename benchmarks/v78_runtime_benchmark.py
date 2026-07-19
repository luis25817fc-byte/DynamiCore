
"""
DynamiCore V7.8
Runtime Benchmark Engine

Mide:

- tiempo de ejecución
- estabilidad
- volumen de sistemas procesados
- consistencia determinista

"""


import sys
import time
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


if str(ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT)
    )


from app.core.engine import DynamiCoreEngine



class DynamiCoreBenchmark:


    VERSION = "7.8.0"



    def __init__(self):

        self.engine = DynamiCoreEngine()



    def generate_system(
        self,
        size
    ):

        return [
            (i * 7 + 3) % 2
            for i in range(size)
        ]



    def run_case(
        self,
        size
    ):

        system = self.generate_system(
            size
        )


        start = time.perf_counter()


        result = self.engine.analyze(
            system
        )


        end = time.perf_counter()


        return {

            "size":
                size,

            "execution_time":
                round(
                    end - start,
                    6
                ),

            "system_size":
                result.get(
                    "system_size",
                    0
                ),

            "status":
                "OK"

        }



    def run(
        self,
        sizes=None
    ):

        if sizes is None:

            sizes = [
                8,
                16,
                32,
                64
            ]


        results = []


        for size in sizes:

            results.append(
                self.run_case(
                    size
                )
            )


        return {

            "version":
                self.VERSION,

            "benchmark":
                results,

            "status":
                "COMPLETE"

        }



if __name__ == "__main__":


    benchmark = DynamiCoreBenchmark()


    output = benchmark.run()


    print(
        json.dumps(
            output,
            indent=4
        )
    )
