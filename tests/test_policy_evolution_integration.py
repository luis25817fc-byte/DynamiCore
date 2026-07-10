
import sys

sys.path.insert(
    0,
    "/content/DynamiCore"
)


from app.core.adaptation.policy_evolution import PolicyEvolutionEngine
from app.core.adaptation.policy_bridge import PolicyBridge



def test_policy_evolution_flow():

    evolution = PolicyEvolutionEngine()

    bridge = PolicyBridge(
        evolution
    )


    bridge.update(
        "reinforce_strategy",
        {
            "outcome": "successful"
        }
    )


    bridge.update(
        "reinforce_strategy",
        {
            "outcome": "successful"
        }
    )


    bridge.update(
        "collect_more_information",
        {
            "outcome": "failed"
        }
    )


    ranking = evolution.rank()

    best = evolution.best_policy()


    assert ranking[0]["policy"] == "reinforce_strategy"

    assert best["policy"] == "reinforce_strategy"

    assert best["confidence"] == 1.0


    return {

        "ranking": ranking,

        "best_policy": best

    }



if __name__ == "__main__":

    result = test_policy_evolution_flow()

    print(
        "✅ POLICY EVOLUTION INTEGRATION TEST OK"
    )

    print(result)
