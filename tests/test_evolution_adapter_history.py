
import sys

sys.path.insert(
    0,
    "/content/DynamiCore"
)


from app.core.adaptation.evolution_adapter import EvolutionAdapter



def test_evolution_history():

    adapter = EvolutionAdapter()


    adapter.process(
        "reinforce_strategy",
        {
            "outcome": "successful"
        }
    )


    adapter.process(
        "reinforce_strategy",
        {
            "outcome": "successful"
        }
    )


    adapter.process(
        "replace_strategy",
        {
            "outcome": "failed"
        }
    )


    best = adapter.evolution.best_policy()


    assert best["policy"] == "reinforce_strategy"


    assert True



if __name__ == "__main__":

    print(
        test_evolution_history()
    )