

class PolicyEvolutionEngine:


    def __init__(self):

        self.version = "6.1"

        self.policies = {}



    def record(

        self,

        policy,

        outcome

    ):


        if policy not in self.policies:

            self.policies[policy] = {


                "uses": 0,

                "success": 0,

                "failed": 0

            }



        data = self.policies[policy]


        data["uses"] += 1



        if outcome == "successful":

            data["success"] += 1


        elif outcome == "failed":

            data["failed"] += 1



        return data



    def rank(self):


        ranking = []



        for name, data in self.policies.items():


            uses = data["uses"]


            rate = 0


            if uses > 0:

                rate = data["success"] / uses



            ranking.append(

                {

                    "policy": name,

                    "success_rate": round(

                        rate,

                        3

                    ),

                    "uses": uses

                }

            )



        ranking.sort(

            key=lambda x: x["success_rate"],

            reverse=True

        )


        return ranking



    def best_policy(self):


        ranking = self.rank()



        if not ranking:

            return {

                "policy": "none",

                "confidence": 0

            }



        return {


            "policy":

                ranking[0]["policy"],


            "confidence":

                ranking[0]["success_rate"]

        }
