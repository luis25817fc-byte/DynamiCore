
class CausalGraph:


    def __init__(self):

        self.nodes = {}



    def add_relation(
        self,
        cause,
        effect,
        weight
    ):

        if cause not in self.nodes:
            self.nodes[cause] = []


        self.nodes[cause].append({

            "effect": effect,

            "weight": weight

        })



    def get_effects(self, cause):

        return self.nodes.get(
            cause,
            []
        )
