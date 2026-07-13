
from app.core.enterprise.knowledge_memory import EnterpriseKnowledgeMemory
from app.core.enterprise.persistence_history import EnterprisePersistenceHistory

from app.core.graph_intelligence.temporal_memory import TemporalGraphMemory
from app.core.graph_intelligence.pattern_engine import StructuralPatternEngine
from app.core.graph_intelligence.history_engine import HistoricalEvolutionEngine
from app.core.graph_intelligence.transition_memory import TransitionMemory


class CognitiveMemoryLayer:

    VERSION = "6.9.4"


    def __init__(self):

        self.knowledge = EnterpriseKnowledgeMemory()

        self.persistence = EnterprisePersistenceHistory()

        self.temporal = TemporalGraphMemory()

        self.patterns = StructuralPatternEngine()

        self.history = HistoricalEvolutionEngine()

        self.transitions = TransitionMemory()



    def process(
        self,
        signature,
        state,
        before=None,
        after=None,
        diff=None,
        structural_intelligence=None,
        evolution=None,
        prediction=None,
        decision=None
    ):

        pattern = self.patterns.detect(
            signature
        )


        self.knowledge.learn(
            pattern
        )


        self.persistence.save(
            state
        )


        self.temporal.store(
            signature
        )


        self.history.record(
            signature,
            structural_intelligence,
            evolution,
            prediction,
            decision
        )


        if before is not None:

            self.transitions.record(
                before,
                after,
                diff
            )


        return {

            "version": self.VERSION,

            "status": "COGNITIVE_MEMORY_ACTIVE",

            "pattern": pattern,

            "knowledge": self.knowledge.recall(),

            "history_size": self.history.size(),

            "transitions": self.transitions.history()

        }
