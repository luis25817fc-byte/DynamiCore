
from app.core.enterprise.autonomous_control import EnterpriseAutonomousControl
from app.core.enterprise.workflow_engine import EnterpriseWorkflowEngine
from app.core.enterprise.decision_service import EnterpriseDecisionService
from app.core.decision.engine import DecisionEngine
from app.core.agents.decision_agent import DecisionAgent


class AutonomousIntelligenceLoop:

    VERSION = "6.9.2"


    def __init__(self):

        self.workflow = EnterpriseWorkflowEngine()

        self.decision_service = EnterpriseDecisionService()

        self.decision_engine = DecisionEngine()

        self.agent = DecisionAgent()

        self.control = None



    def initialize_control(self, adaptive):

        self.control = EnterpriseAutonomousControl(
            adaptive,
            self.workflow
        )



    def process(self, intelligence_state):

        decision = self.decision_service.evaluate(
            intelligence_state
        )


        action = self.agent.run(
            decision
        )


        workflow_result = self.workflow.execute(
            action,
            decision
        )


        return {

            "version": self.VERSION,

            "status": "AUTONOMOUS_LOOP_ACTIVE",

            "decision": decision,

            "action": action,

            "workflow": workflow_result

        }
