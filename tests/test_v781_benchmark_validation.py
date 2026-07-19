
"""
DynamiCore V7.8.1
Benchmark Validation Suite

Validaciones:

- Import del benchmark
- Ejecución completa
- Repetibilidad
- Integridad de resultados
- Escalamiento básico

"""


import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


if str(ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT)
    )


from benchmarks.v78_runtime_benchmark import DynamiCoreBenchmark



def test_benchmark_import():

    benchmark = DynamiCoreBenchmark()

    assert benchmark is not None



def test_benchmark_execution():

    benchmark = DynamiCoreBenchmark()


    result = benchmark.run(
        sizes=[
            8,
            16,
            32
        ]
    )


    assert result["status"] == "COMPLETE"

    assert len(
        result["benchmark"]
    ) == 3



def test_benchmark_repeatability():

    benchmark = DynamiCoreBenchmark()


    first = benchmark.run(
        sizes=[
            8,
            16
        ]
    )


    second = benchmark.run(
        sizes=[
            8,
            16
        ]
    )


    assert first["status"] == second["status"]

    assert len(
        first["benchmark"]
    ) == len(
        second["benchmark"]
    )



def test_benchmark_integrity():

    benchmark = DynamiCoreBenchmark()


    result = benchmark.run(
        sizes=[
            8,
            64
        ]
    )


    for item in result["benchmark"]:

        assert item["status"] == "OK"

        assert item["system_size"] == item["size"]

        assert item["execution_time"] >= 0



if __name__ == "__main__":

    print(
        "DynamiCore V7.8.1 Benchmark Validation ONLINE"
    )

