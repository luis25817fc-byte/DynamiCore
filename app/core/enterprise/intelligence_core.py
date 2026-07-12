
class DynamiCoreEnterpriseIntelligenceCore:

    VERSION = "6.8.0"


    def __init__(
        self,
        enterprise_core,
        graph_engine,
        decision_service,
        memory
    ):

        self.enterprise_core = enterprise_core
        self.graph_engine = graph_engine
        self.decision_service = decision_service
        self.memory = memory


    def analyze(
        self,
        previous,
        current
    ):

        graph = self.graph_engine.run(
            previous,
            current
        )


        decision = self.decision_service.generate(
            graph
        )


        self.memory.learn(
            {
                "graph_state": graph,
                "decision": decision
            }
        )


        return {

            "version":
                self.VERSION,

            "status":
                "ENTERPRISE_INTELLIGENCE_ACTIVE",

            "graph":
                graph,

            "decision":
                decision,

            "memory":
                self.memory.recall()
        }
