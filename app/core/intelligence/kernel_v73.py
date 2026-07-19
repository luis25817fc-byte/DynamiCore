
from datetime import datetime

from app.core.intelligence.dlis_state import DLISState
from app.core.intelligence.validation_bridge import ValidationBridgeV73



class IntelligenceKernelV73:


    VERSION = "7.3"



    def __init__(
        self,
        mathematical_core=None,
        graph_intelligence=None,
        evolution_engine=None,
        validation_bridge=None
    ):

        self.created = datetime.utcnow()

        self.mathematical_core = mathematical_core

        self.graph_intelligence = graph_intelligence

        self.evolution_engine = evolution_engine

        self.validation_bridge = (
            validation_bridge
            if validation_bridge
            else ValidationBridgeV73()
        )


        self.modules = {

            "mathematical_core":
                mathematical_core is not None,

            "graph_intelligence":
                graph_intelligence is not None,

            "evolution_engine":
                evolution_engine is not None,

            "validation_bridge":
                True,

            "enterprise":
                False
        }



    def attach_math_core(self, mathematical_core):

        self.mathematical_core = mathematical_core

        self.modules["mathematical_core"] = True

        return True



    def attach_graph_intelligence(self, graph_intelligence):

        self.graph_intelligence = graph_intelligence

        self.modules["graph_intelligence"] = True

        return True



    def attach_evolution_engine(self, evolution_engine):

        self.evolution_engine = evolution_engine

        self.modules["evolution_engine"] = True

        return True



    def attach_validation_bridge(self, bridge):

        self.validation_bridge = bridge

        self.modules["validation_bridge"] = True

        return True



    def analyze(self, previous_state, current_state):

        result = {
            "version": self.VERSION,
            "status": "ONLINE"
        }


        if self.mathematical_core:

            result["mathematical"] = (
                self.mathematical_core.analyze(
                    previous_state,
                    current_state
                )
            )


        if self.graph_intelligence:

            result["graph"] = (
                self.graph_intelligence.analyze(
                    previous_state,
                    current_state
                )
            )


        if self.evolution_engine:

            result["evolution"] = (
                self.evolution_engine.evolve(
                    current_state
                )
            )


        return result



    def build_state(self, previous_state, current_state):

        analysis = self.analyze(
            previous_state,
            current_state
        )


        return DLISState(

            mathematical_state=
                analysis.get("mathematical"),

            graph_state=
                analysis.get("graph"),

            evolution_state=
                analysis.get("evolution"),

            global_entropy=
                getattr(
                    current_state,
                    "entropy",
                    0.0
                ),

            structural_health=
                getattr(
                    current_state,
                    "resilience",
                    0.0
                ),

            transition_risk=
                getattr(
                    current_state,
                    "divergence",
                    0.0
                ),

            system_status="ONLINE"
        )



    def validate(self, state):

        return self.validation_bridge.validate(
            state
        )





    def attach_enterprise_layer(
        self,
        enterprise_layer
    ):

        self.enterprise_layer = enterprise_layer

        self.modules["enterprise"] = True

        return True


    def status(self):

        active = sum(
            1
            for value in self.modules.values()
            if value
        )

        total = len(self.modules)


        return {

            "version": self.VERSION,

            "modules": self.modules,

            "health":
                active / total,

            "status":
                "ONLINE"
                if active == total
                else "DEGRADED"
        }
