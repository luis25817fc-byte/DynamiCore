
from datetime import datetime

from app.core.mathematical.invariant_engine import InvariantEngine


class MathematicalCore:

    VERSION = "7.3"

    def __init__(self):

        self.invariant_engine = InvariantEngine()

        self.status_state = "ONLINE"


    def analyze(
        self,
        previous_state,
        current_state
    ):

        invariant_report = self.invariant_engine.compare(
            previous_state,
            current_state
        )


        return {

            "version": self.VERSION,

            "timestamp": datetime.utcnow(),

            "mathematical_state": {

                "previous": previous_state.__dict__,

                "current": current_state.__dict__

            },

            "invariant_analysis": invariant_report.__dict__,

            "status": self.status_state

        }


    def status(self):

        return {

            "version": self.VERSION,

            "module": "MathematicalCore",

            "invariant_engine": True,

            "status": self.status_state

        }
