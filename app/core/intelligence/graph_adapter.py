
from app.core.graph_intelligence.structural_signature import (
    StructuralSignatureEngine
)

from app.core.graph_intelligence.graph_delta import (
    GraphDeltaEngine
)


class GraphIntelligenceAdapter:


    def __init__(self):

        self.signature_engine = StructuralSignatureEngine()

        self.delta_engine = GraphDeltaEngine()


    def analyze_structure(
        self,
        graph
    ):

        signature = None
        delta = None


        try:
            signature = self.signature_engine.generate(
                graph
            )

        except Exception as e:
            signature = {
                "error":str(e)
            }


        try:
            delta = self.delta_engine.compare(
                graph
            )

        except Exception as e:
            delta = {
                "error":str(e)
            }


        return {

            "structural_signature": signature,

            "graph_delta": delta

        }
