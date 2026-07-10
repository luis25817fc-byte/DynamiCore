
from .memory import LearningMemory



class LearningEngine:


    def __init__(self):

        self.memory = LearningMemory()



    def learn(
        self,
        state,
        context,
        decision,
        explanation
    ):


        case = {


            "state":
                state.to_dict(),


            "context":
                context,


            "decision":
                decision,


            "explanation":
                explanation

        }


        self.memory.store(case)


        return {


            "stored": True,

            "memory_size":
                self.memory.count()

        }



    def recall(self):

        return self.memory.all()
