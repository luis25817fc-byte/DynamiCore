from .graph_delta import GraphDeltaEngine
from .structural_signature import StructuralSignatureEngine
from .structural_signature_v2 import StructuralSignatureV2
from .evolution_layer import EvolutionLayer
from .evolution_diff import EvolutionDiffEngine
from .transition_detector import TransitionDetector
from .graph_intelligence import DynamicGraphIntelligence
from .evolution_metrics import EvolutionMetrics
from .structural_transition import StructuralTransitionIntelligence
from .structural_fusion import StructuralIntelligenceFusion
from .predictive_structural import PredictiveStructuralLayer
from .critical_transition import CriticalTransitionDetector
from .dynamic_intelligence_state import DynamicIntelligenceState
from .intelligence_validator import IntelligenceValidator
from .intelligence_benchmark import IntelligenceBenchmark
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
        self.transition_detector = TransitionDetector()
        self.graph_intelligence = DynamicGraphIntelligence()
        self.evolution_metrics = EvolutionMetrics()
        self.structural_transition = StructuralTransitionIntelligence()
        self.structural_fusion = StructuralIntelligenceFusion()
        self.predictive_structural = PredictiveStructuralLayer()
        self.critical_transition = CriticalTransitionDetector()
        self.dynamic_state = DynamicIntelligenceState()
        self.validator = IntelligenceValidator()
        self.benchmark = IntelligenceBenchmark()
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

        evolution_diff = self.evolution_diff.compare(
            previous,
            current
        )

        transition = self.transition_detector.detect(
            evolution_diff
        )

        graph_state = self.graph_intelligence.analyze(
            evolution_diff,
            transition
        )

        evolution_metrics = self.evolution_metrics.calculate(
            evolution_diff,
            transition
        )

        transition_intelligence = self.structural_transition.analyze(
            sig,
            evolution_metrics
        )


        decision = self.decision.analyze(
            intelligence,
            evo,
            prediction
        )

        self.memory.store(sig)

        structural_fusion = self.structural_fusion.fuse(
            sig,
            evolution_metrics,
            transition_intelligence,
            graph_state,
            decision
        )

        predictive_structural = self.predictive_structural.predict(
            structural_fusion,
            self.history
        )

        critical_transition = self.critical_transition.analyze(
            evolution_metrics,
            predictive_structural,
            transition_intelligence
        )

        dynamic_state = self.dynamic_state.build(
            structural_fusion,
            predictive_structural,
            critical_transition,
            decision
        )

        validation_report = self.validator.validate({
            "signature": sig,
            "evolution": evo,
            "predictive_structural": predictive_structural,
            "critical_transition": critical_transition,
            "decision": decision,
            "structural_fusion": structural_fusion,
            "dynamic_state": dynamic_state
        })

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
            "evolution_diff": evolution_diff,
            "transition": transition,
            "graph_intelligence": graph_state,
            "evolution_metrics": evolution_metrics,
            "transition_intelligence": transition_intelligence,
            "structural_fusion": structural_fusion,
            "predictive_structural": predictive_structural,
            "critical_transition": critical_transition,
            "dynamic_state": dynamic_state,
            "validation_report": validation_report,
            "decision": decision,
            "history": history_snapshot
        }
