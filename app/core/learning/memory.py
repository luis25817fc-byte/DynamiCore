
class LearningMemory:


    def __init__(self):

        self.cases = []



    def store(self, case):

        self.cases.append(case)



    def all(self):

        return self.cases



    def count(self):

        return len(self.cases)
