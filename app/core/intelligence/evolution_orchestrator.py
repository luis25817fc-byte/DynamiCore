
from datetime import datetime

from app.core.intelligence.evolution_engine import EvolutionEngine
from app.core.intelligence.graph_evolution_bridge import GraphEvolutionBridge


class EvolutionOrchestrator:

    VERSION = "7.2"

    def __init__(self):

        self.engine = EvolutionEngine()
        self.bridge = GraphEvolutionBridge()


    def analyze_evolution(
        self,
        system_id,
        previous_state,
        current_state
    ):

        report = self.engine.analyze(
            system_id,
            previous_state,
            current_state
        )

        graph_result = self.bridge.process(
            report
        )

        return {
            "version": self.VERSION,
            "timestamp": datetime.utcnow(),
            "system_id": system_id,
            "evolution": report,
            "graph_evolution": graph_result,
            "status": "ONLINE"
        }


    def status(self):

        return {
            "version": self.VERSION,
            "engine": True,
            "bridge": True,
            "status": "ONLINE"
        }
