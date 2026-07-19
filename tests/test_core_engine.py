
import sys

sys.path.insert(0, "/content/DynamiCore")

from app.core.engine import DynamiCoreEngine


def test_core_engine():

    result = DynamiCoreEngine().analyze([0,1,2,3,4])

    assert "H(k)" in result
    assert "R(k)" in result
    assert "ΔR(k)" in result
    assert "Ψ(k)" in result
    assert "D(k)" in result

    assert "alert_level" in result
    assert "regime" in result


if __name__ == "__main__":
    test_core_engine()
    print("✅ Core Engine OK")
