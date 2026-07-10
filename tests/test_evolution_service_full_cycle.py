
import sys

sys.path.insert(
    0,
    "/content/DynamiCore"
)


from app.core.adaptation.evolution_service import EvolutionService



def test_full_cycle():

    service = EvolutionService()


    cycles = [

        (
            "reinforce_strategy",
            "successful"
        ),

        (
            "reinforce_strategy",
            "successful"
        ),

        (
            "replace_strategy",
            "failed"
        )

    ]


    for policy, outcome in cycles:

        service.evaluate(

            policy,

            {
                "outcome": outcome
            }

        )


    recommendation = service.recommendation()


    assert recommendation["policy"] == "reinforce_strategy"


    return {

        "recommendation": recommendation,

        "ranking":

            service.adapter.evolution.rank()

    }



if __name__ == "__main__":

    print(
        test_full_cycle()
    )
