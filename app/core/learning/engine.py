
from .memory import LearningMemory


class LearningEngine:


    def __init__(self):

        self.memory = LearningMemory()



    def learn(self, case):

        self.memory.store(case)


        return {

            "stored": True,

            "memory_size":
                self.memory.count()

        }



    def recall(self):

        return self.memory.all()
