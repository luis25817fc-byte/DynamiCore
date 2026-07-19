
from datetime import datetime


class GraphIntelligenceValidator:

    VERSION = "7.3"

    def __init__(self):
        self.checks = {}


    def validate_graph_state(self, state):

        required = [
            "nodes",
            "cycles",
            "basins"
        ]

        result = all(
            key in state
            for key in required
        )

        self.checks["graph_state"] = result

        return result


    def validate_evolution(self, evolution):

        required = [
            "previous_state",
            "current_state",
            "delta",
            "transition",
            "confidence"
        ]

        result = all(
            hasattr(evolution, key)
            for key in required
        )

        self.checks["evolution"] = result

        return result


    def validate_prediction(self, prediction):

        required = [
            "risk_level",
            "confidence",
            "early_warning"
        ]

        if isinstance(prediction, dict):
            result = all(
                key in prediction
                for key in required
            )
        else:
            result = all(
                hasattr(prediction, key)
                for key in required
            )

        self.checks["prediction"] = result

        return result


    def validate_decision(self, decision):

        if isinstance(decision, dict):

            result = "action" in decision

        else:

            result = hasattr(
                decision,
                "action"
            )

        self.checks["decision"] = result

        return result


    def validate(self, payload):

        self.checks = {}

        self.validate_graph_state(
            payload.get(
                "graph_state",
                {}
            )
        )

        if payload.get("evolution"):
            self.validate_evolution(
                payload["evolution"]
            )

        self.validate_prediction(
            payload.get(
                "prediction",
                {}
            )
        )

        self.validate_decision(
            payload.get(
                "decision",
                {}
            )
        )

        passed = all(
            self.checks.values()
        )

        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.utcnow(),

            "checks":
                self.checks,

            "passed":
                passed,

            "status":
                "READY"
                if passed
                else "FAILED"
        }


    def status(self):

        return {

            "version":
                self.VERSION,

            "checks":
                self.checks,

            "status":
                "ONLINE"
        }
