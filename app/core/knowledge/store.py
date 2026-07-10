
class KnowledgeStore:


    def __init__(self):

        self.patterns = []
        self.rules = []



    def add_pattern(
        self,
        pattern
    ):

        self.patterns.append(pattern)



    def add_rule(
        self,
        rule
    ):

        self.rules.append(rule)



    def get_patterns(self):

        return self.patterns



    def get_rules(self):

        return self.rules
