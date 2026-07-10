

class StrategyMemory:


    def __init__(self):

        self.version = "6.0"

        self.memory = []



    def store(

        self,

        decision,

        policy,

        outcome,

        impact,

        confidence

    ):


        record = {


            "decision":

                decision,


            "policy":

                policy,


            "outcome":

                outcome,


            "impact":

                impact,


            "confidence":

                confidence

        }



        self.memory.append(

            record

        )


        return {


            "stored":

                True,


            "memory_size":

                len(

                    self.memory

                )

        }



    def all(self):

        return self.memory



    def count(self):

        return len(

            self.memory

        )
