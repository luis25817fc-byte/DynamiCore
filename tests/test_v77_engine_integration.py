
"""
DynamiCore V7.7.7
Engine Integration Validation

Validación:

DynamiCoreEngine
        |
MasterEngineBridge
        |
MasterOrchestrationLayer
        |
CanonicalEngineBinding

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


def test_engine_import():

    engine = DynamiCoreEngine()

    assert engine is not None


def test_bridge_import():

    bridge = MasterEngineBridge()

    assert bridge.status()["status"] == "ONLINE"


def test_orchestrator_import():

    orch = MasterOrchestrationLayer()

    assert orch.status()["status"] == "ONLINE"


def test_binding_import():

    binding = CanonicalEngineBinding()

    assert binding.status()["status"] == "ONLINE"


def test_full_contract_chain():

    engine = DynamiCoreEngine()

    bridge = MasterEngineBridge(
        engine=engine
    )

    orch = MasterOrchestrationLayer(
        engine=engine
    )

    binding = CanonicalEngineBinding(
        engine=engine,
        bridge=bridge,
        orchestrator=orch
    )

    result = binding.status()

    assert result["status"] == "ONLINE"


if __name__ == "__main__":

    print(
        "DynamiCore V7.7.7 Integration Validation ONLINE"
    )
