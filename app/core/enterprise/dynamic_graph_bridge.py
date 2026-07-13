
from app.core.graph_intelligence.graph_intelligence import DynamicGraphIntelligence
from app.core.graph_intelligence.structural_fusion import StructuralIntelligenceFusion
from app.core.graph_intelligence.dynamic_intelligence_state import DynamicIntelligenceState


class EnterpriseDynamicGraphBridge:

    VERSION = "6.9.0"


    def __init__(self, enterprise_core=None):

        self.enterprise_core = enterprise_core

        self.graph_intelligence = DynamicGraphIntelligence()

        self.structural_fusion = StructuralIntelligenceFusion()

        self.dynamic_state = DynamicIntelligenceState()



    def analyze_transition(self, diff, transition):

        graph_result = self.graph_intelligence.analyze(
            diff,
            transition
        )


        fusion = self.structural_fusion.fuse(
            graph_result.get("signature", {}),
            graph_result.get("evolution_metrics", {}),
            graph_result.get("transition_intelligence", {}),
            graph_result,
            graph_result.get("decision", {})
        )


        dynamic_state = self.dynamic_state.build(
            fusion,
            graph_result.get("predictive_structural", {}),
            graph_result.get("critical_transition", {}),
            graph_result.get("decision", {})
        )


        return {
            "version": self.VERSION,
            "status": "DYNAMIC_GRAPH_BRIDGE_ACTIVE",
            "graph_result": graph_result,
            "fusion": fusion,
            "dynamic_state": dynamic_state
        }
