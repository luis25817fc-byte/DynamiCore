

class AdaptiveLearningEngine:


    def __init__(self):

        self.version = "6.0"

        self.history = []



    def analyze(

        self,

        memories

    ):


        if not memories:

            return {

                "learned": False,

                "reason": "no_memory"

            }



        total = len(
            memories
        )


        successful = 0

        failed = 0


        policies = {}



        for item in memories:


            outcome = item.get(

                "outcome",

                "unknown"

            )


            policy = item.get(

                "policy",

                "unknown"

            )


            if outcome == "successful":

                successful += 1


            elif outcome == "failed":

                failed += 1



            if policy not in policies:

                policies[policy] = 0


            policies[policy] += 1



        success_rate = successful / total



        result = {


            "version":

                self.version,


            "learned":

                True,


            "total_cases":

                total,


            "successful":

                successful,


            "failed":

                failed,


            "success_rate":

                round(

                    success_rate,

                    3

                ),


            "policy_usage":

                policies

        }



        self.history.append(

            result

        )


        return result
