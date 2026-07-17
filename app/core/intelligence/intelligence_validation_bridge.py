
from datetime import datetime

from app.core.intelligence.graph_intelligence_validator import (
    GraphIntelligenceValidator
)


class IntelligenceValidationBridge:

    VERSION = "7.3"


    def __init__(self):

        self.validator = GraphIntelligenceValidator()

        self.connected = True


    def validate_intelligence(self, intelligence_report):

        payload = {

            "graph_state":
                intelligence_report.get(
                    "graph_state",
                    {}
                ),

            "evolution":
                intelligence_report.get(
                    "evolution"
                ),

            "prediction":
                intelligence_report.get(
                    "prediction",
                    {}
                ),

            "decision":
                intelligence_report.get(
                    "decision",
                    {}
                )
        }


        validation = self.validator.validate(
            payload
        )


        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.utcnow(),

            "validation":
                validation,

            "status":
                "ONLINE"
                if validation["passed"]
                else "FAILED"
        }


    def status(self):

        return {

            "version":
                self.VERSION,

            "validator":
                True,

            "connected":
                self.connected,

            "status":
                "ONLINE"
        }
