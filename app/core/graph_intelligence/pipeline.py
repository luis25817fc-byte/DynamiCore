
from .graph_delta import GraphDeltaEngine
from .structural_signature import StructuralSignatureEngine
from .evolution_layer import EvolutionLayer
from .pattern_engine import StructuralPatternEngine
from .evolution_predictor import GraphEvolutionPredictor
from .temporal_memory import TemporalGraphMemory


class GraphIntelligencePipeline:

    VERSION="6.2.6"

    def __init__(self):
        self.delta=GraphDeltaEngine()
        self.signature=StructuralSignatureEngine()
        self.evolution=EvolutionLayer()
        self.patterns=StructuralPatternEngine()
        self.predictor=GraphEvolutionPredictor()
        self.memory=TemporalGraphMemory()


    def run(self,previous,current):

        sig=self.signature.generate(current)

        delta=self.delta.compare(previous,current)

        evo=self.evolution.analyze(previous,current)

        patterns=self.patterns.detect({
            **sig,
            "evolution_score":evo["evolution_score"]
        })

        prediction=self.predictor.predict({
            **sig,
            "evolution_score":evo["evolution_score"]
        })

        self.memory.store(sig)

        return {
            "version":self.VERSION,
            "signature":sig,
            "delta":delta,
            "evolution":evo,
            "patterns":patterns,
            "prediction":prediction
        }
