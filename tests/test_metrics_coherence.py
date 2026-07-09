
import sys
sys.path.insert(0,"/content/DynamiCore")

from app.core.metrics.coherence import CoherenceEngine

def test_coherence():
    r = CoherenceEngine().compute([0,1,2])
    assert "R(k)" in r

if __name__=="__main__":
    test_coherence()
    print("✅ Coherence OK")
