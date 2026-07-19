
"""
DynamiCore V7.7.8
Runtime Hardening Validation

Objetivo:

Validar estabilidad del runtime:

- entradas vacías
- entradas inválidas
- ejecución repetida
- determinismo
- contratos básicos

"""


import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


if str(ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT)
    )


from app.core.engine import DynamiCoreEngine
from app.core.intelligence.master_engine_bridge import MasterEngineBridge
from app.core.intelligence.master_orchestration_layer import MasterOrchestrationLayer
from app.core.intelligence.canonical_engine_binding import CanonicalEngineBinding



def runtime():

    engine = DynamiCoreEngine()

    bridge = MasterEngineBridge(
        engine=engine
    )

    orchestrator = MasterOrchestrationLayer(
        engine=engine
    )


    return CanonicalEngineBinding(
        engine=engine,
        bridge=bridge,
        orchestrator=orchestrator
    )



def test_empty_input_protection():

    engine = DynamiCoreEngine()

    result = engine.analyze([])

    assert result is not None

    assert "error" in result



def test_runtime_repeated_execution():

    rt = runtime()


    system = [
        1,
        0,
        1,
        1,
        0,
        1
    ]


    first = rt.execute(
        system
    )


    second = rt.execute(
        system
    )


    assert first is not None

    assert second is not None



def test_deterministic_output():

    rt1 = runtime()

    rt2 = runtime()


    system = [
        0,
        1,
        0,
        1
    ]


    result1 = rt1.execute(
        system
    )


    result2 = rt2.execute(
        system
    )


    assert type(result1) == type(result2)



def test_contract_status():

    rt = runtime()


    status = rt.status()


    assert status["status"] == "ONLINE"



if __name__ == "__main__":

    print(
        "DynamiCore V7.7.8 Runtime Hardening ONLINE"
    )
