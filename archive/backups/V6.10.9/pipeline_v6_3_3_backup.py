from .graph_delta import GraphDeltaEngine
from .structural_signature import StructuralSignatureEngine
from .evolution_layer import EvolutionLayer
from .pattern_engine import StructuralPatternEngine
from .evolution_predictor import GraphEvolutionPredictor
from .temporal_memory import TemporalGraphMemory


class GraphIntelligencePipeline:

    VERSION = "6.3.2"

    def __init__(self):
        self.delta = GraphDeltaEngine()
        self.signature = StructuralSignatureEngine()
        self.evolution = EvolutionLayer()
        self.patterns = StructuralPatternEngine()
        self.predictor = GraphEvolutionPredictor()
        self.memory = TemporalGraphMemory()


    def analyze_structure(self, sig):

        complexity = sig.get("structural_complexity", 0)
        stability = sig.get("stability_index", 1)
        density = sig.get("density", 0)

        if complexity > 1:
            risk = "HIGH"
        elif complexity > 0.5:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        return {
            "density": density,
            "complexity": complexity,
            "stability": stability,
            "structural_risk": risk
        }


    def run(self, previous, current):

        sig = self.signature.generate(current)

        intelligence = self.analyze_structure(sig)

        delta = self.delta.compare(previous, current)

        evo = self.evolution.analyze(previous, current)

        patterns = self.patterns.detect({
            **sig,
            "evolution_score": evo["evolution_score"]
        })

        prediction = self.predictor.predict({
            **sig,
            "evolution_score": evo["evolution_score"]
        })

        self.memory.store(sig)

        return {
            "version": self.VERSION,
            "signature": sig,
            "structural_intelligence": intelligence,
            "delta": delta,
            "evolution": evo,
            "patterns": patterns,
            "prediction": prediction
        }
