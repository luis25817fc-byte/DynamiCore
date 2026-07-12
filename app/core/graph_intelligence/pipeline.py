from .graph_delta import GraphDeltaEngine
from .structural_signature import StructuralSignatureEngine
from .structural_signature_v2 import StructuralSignatureV2
from .evolution_layer import EvolutionLayer
from .evolution_diff import EvolutionDiffEngine
from .pattern_engine import StructuralPatternEngine
from .evolution_predictor import GraphEvolutionPredictor
from .temporal_memory import TemporalGraphMemory
from .history_engine import HistoricalEvolutionEngine
from .decision_engine import DecisionEngine


class GraphIntelligencePipeline:

    VERSION = "6.4.0"

    def __init__(self):
        self.delta = GraphDeltaEngine()
        self.signature = StructuralSignatureEngine()
        self.signature_v2 = StructuralSignatureV2()
        self.evolution = EvolutionLayer()
        self.evolution_diff = EvolutionDiffEngine()
        self.patterns = StructuralPatternEngine()
        self.predictor = GraphEvolutionPredictor()
        self.memory = TemporalGraphMemory()
        self.history = HistoricalEvolutionEngine()
        self.decision = DecisionEngine()


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

        decision = self.decision.analyze(
            intelligence,
            evo,
            prediction
        )

        self.memory.store(sig)

        history_snapshot = self.history.record(
            sig,
            intelligence,
            evo,
            prediction,
            decision
        )

        return {
            "version": self.VERSION,
            "signature": sig,
            "structural_intelligence": intelligence,
            "delta": delta,
            "evolution": evo,
            "patterns": patterns,
            "prediction": prediction,
            "decision": decision,
            "history": history_snapshot
        }
