
import sys
sys.path.insert(0,"/content/DynamiCore")

from app.core.metrics.divergence import DivergenceEngine


def test_divergence():

    r = DivergenceEngine().analyze(
        5,
        3,
        4
    )

    assert "D(k)" in r


if __name__=="__main__":
    test_divergence()
    print("✅ Divergence OK")
