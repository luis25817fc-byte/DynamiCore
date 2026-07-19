
class StructuralMemory:

    VERSION = "6.5.0"

    def __init__(self):
        self.memory = []

    def store(self, signature):
        self.memory.append(signature)

    def size(self):
        return len(self.memory)
