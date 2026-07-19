
"""
DynamiCore V7.7.7
Runtime Pipeline Validation

Validación del flujo:

INPUT
 |
CanonicalEngineBinding
 |
MasterEngineBridge
 |
MasterOrchestrationLayer
 |
DynamiCoreEngine
 |
OUTPUT

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



def build_runtime():

    engine = DynamiCoreEngine()

    bridge = MasterEngineBridge(
        engine=engine
    )

    orchestrator = MasterOrchestrationLayer(
        engine=engine
    )


    binding = CanonicalEngineBinding(
        engine=engine,
        bridge=bridge,
        orchestrator=orchestrator
    )


    return binding



def test_runtime_creation():

    runtime = build_runtime()

    assert runtime.status()["status"] == "ONLINE"



def test_runtime_execution():

    runtime = build_runtime()


    system = [
        0,
        1,
        1,
        0,
        1,
        0,
        1,
        1
    ]


    result = runtime.execute(
        system
    )


    assert result is not None

    assert "binding" in result



def test_pipeline_trace():

    runtime = build_runtime()


    system = [
        1,
        0,
        1,
        0
    ]


    runtime.execute(
        system
    )


    trace = runtime.trace


    assert len(trace) > 0


    stages = [
        x["stage"]
        for x in trace
    ]


    assert "INPUT_RECEIVED" in stages



if __name__ == "__main__":

    print(
        "DynamiCore V7.7.7 Runtime Pipeline ONLINE"
    )
