
import sys
sys.path.insert(0,"/content/DynamiCore")

from app.core.metrics.dynamics import DynamicsEngine

def test_dynamics():
    r = DynamicsEngine().analyze([0,1,2,3,4])
    assert "trend" in r

if __name__=="__main__":
    test_dynamics()
    print("✅ Dynamics OK")
