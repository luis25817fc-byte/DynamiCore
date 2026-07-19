
from datetime import datetime


class GraphEvolutionBridge:

    VERSION = "7.2"


    def __init__(self):

        self.connected = True


    def process(self, evolution_report):

        return {

            "version": self.VERSION,

            "timestamp": datetime.utcnow(),

            "transition":
                getattr(
                    evolution_report,
                    "transition",
                    "UNKNOWN"
                ),

            "confidence":
                getattr(
                    evolution_report,
                    "confidence",
                    0.0
                ),

            "graph_state": {

                "previous":
                    getattr(
                        evolution_report,
                        "previous_state",
                        {}
                    ),

                "current":
                    getattr(
                        evolution_report,
                        "current_state",
                        {}
                    ),

                "delta":
                    getattr(
                        evolution_report,
                        "delta",
                        {}
                    )
            },

            "status": "ONLINE"
        }


    def status(self):

        return {

            "version": self.VERSION,

            "connected": self.connected,

            "status": "ONLINE"
        }
