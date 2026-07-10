
from .store import KnowledgeStore



class KnowledgeEngine:


    def __init__(self):

        self.store = KnowledgeStore()



    def extract(
        self,
        case
    ):


        state = case.get(
            "state",
            {}
        )


        decision = case.get(
            "decision",
            {}
        )


        pattern = {


            "condition": {


                "coherence":
                    state.get(
                        "R(k)",
                        {}
                    ),


                "divergence":
                    state.get(
                        "D(k)",
                        {}
                    )

            },


            "decision":
                decision.get(
                    "decision",
                    "unknown"
                )

        }


        self.store.add_pattern(
            pattern
        )


        return {


            "learned": True,

            "pattern":
                pattern,

            "total_patterns":
                len(
                    self.store.get_patterns()
                )

        }



    def infer(
        self,
        state
    ):


        results = []


        for pattern in self.store.get_patterns():

            results.append({

                "match":
                    True,

                "recommendation":
                    pattern["decision"]

            })


        return results
