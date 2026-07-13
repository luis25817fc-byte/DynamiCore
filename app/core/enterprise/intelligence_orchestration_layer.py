
from app.core.enterprise.orchestrator import EnterpriseOrchestrator
from app.core.enterprise.global_state_manager import EnterpriseGlobalStateManager
from app.core.enterprise.observability import EnterpriseObservability
from app.core.enterprise.monitoring_alert import EnterpriseMonitoringAlert


class IntelligenceOrchestrationLayer:

    VERSION = "6.9.3"


    def __init__(self, orchestrator):

        self.orchestrator = orchestrator

        self.state_manager = EnterpriseGlobalStateManager()

        self.observability = EnterpriseObservability()

        self.monitor = EnterpriseMonitoringAlert()



    def process(self, intelligence_state):

        execution = self.orchestrator.execute(
            intelligence_state
        )


        self.state_manager.update(
            "orchestration",
            execution
        )


        self.observability.record_event()


        alert = self.monitor.analyze(
            execution
        )


        return {

            "version": self.VERSION,

            "status": "ENTERPRISE_ORCHESTRATION_ACTIVE",

            "execution": execution,

            "state": self.state_manager.snapshot(),

            "observability": self.observability.snapshot(),

            "alert": alert

        }
