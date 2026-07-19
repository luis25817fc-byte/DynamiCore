
from datetime import datetime

from .evolution_orchestrator import EvolutionOrchestrator


class IntelligenceCore:

    VERSION = "7.2"


    def __init__(self):

        self.orchestrator = EvolutionOrchestrator()

        self.modules = {
            "graph_adapter": True,
            "evolution_engine": True,
            "graph_evolution_bridge": True
        }


    def analyze(
        self,
        system_id,
        previous_state,
        current_state
    ):

        evolution = self.orchestrator.analyze_evolution(
            system_id,
            previous_state,
            current_state
        )


        return {

            "version": self.VERSION,

            "timestamp": datetime.utcnow(),

            "system_id": system_id,

            "evolution": evolution,

            "status": "ONLINE"
        }


    def status(self):

        active = sum(
            1 for value in self.modules.values()
            if value
        )

        total = len(self.modules)


        return {

            "version": self.VERSION,

            "created": datetime.utcnow(),

            "modules": self.modules,

            "health": active / total,

            "status": "ONLINE"

        }
