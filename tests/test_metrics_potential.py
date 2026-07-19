
import sys
sys.path.insert(0,"/content/DynamiCore")

from app.core.metrics.potential import PotentialEngine

def test_potential():
    r = PotentialEngine().analyze([0,1,2,3,4])
    assert "Ψ(k)" in r

if __name__=="__main__":
    test_potential()
    print("✅ Potential OK")
