
import sys
sys.path.insert(0,"/content/DynamiCore")

from app.core.metrics.entropy import EntropyEngine

def test_entropy():
    e = EntropyEngine()

    assert e.shannon([0,1,2,3]) > 0
    assert e.normalized([0,1,2,3]) >= 0
    assert e.entropy_rate([0,1,2,3]) >= 0

if __name__=="__main__":
    test_entropy()
    print("✅ Entropy OK")
