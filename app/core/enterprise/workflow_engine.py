
class EnterpriseWorkflowEngine:

    VERSION = "6.7.3"


    def __init__(self):

        self.executions = 0


    def execute(
        self,
        event,
        decision
    ):

        self.executions += 1

        action = decision.get(
            "action",
            "NO_ACTION"
        )

        return {

            "version":
                self.VERSION,

            "workflow_status":
                "EXECUTED",

            "execution_id":
                self.executions,

            "event":
                event,

            "action":
                action
        }


    def status(self):

        return {

            "version":
                self.VERSION,

            "executions":
                self.executions,

            "status":
                "ACTIVE"
        }
