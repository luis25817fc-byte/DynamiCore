
class EnterpriseKnowledgeMemory:

    VERSION = "6.7.4"


    def __init__(self):

        self.memory = []


    def learn(
        self,
        pattern
    ):

        self.memory.append(
            pattern
        )

        return {

            "version":
                self.VERSION,

            "learned":
                True,

            "memory_size":
                len(self.memory)
        }


    def recall(self):

        return {

            "version":
                self.VERSION,

            "knowledge_entries":
                len(self.memory),

            "memory":
                self.memory
        }
