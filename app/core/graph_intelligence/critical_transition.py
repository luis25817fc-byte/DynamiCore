
"""
DynamiCore V6.11.1
Critical Transition Intelligence
"""


class CriticalTransitionDetector:


    VERSION = "6.11.1"



    def detect(
        self,
        metrics,
        prediction,
        transition
    ):

        metrics = metrics or {}
        prediction = prediction or {}
        transition = transition or {}


        pressure = metrics.get(
            "evolution_pressure",
            0
        )


        confidence = prediction.get(
            "confidence",
            0
        )


        risk = transition.get(
            "risk",
            "UNKNOWN"
        )



        if pressure >= 5:

            state = "CRITICAL"

        elif pressure >= 2:

            state = "WARNING"

        else:

            state = "STABLE"



        early_warning = (
            state != "STABLE"
        )



        return {

            "version":
                self.VERSION,

            "state":
                state,

            "risk":
                risk,

            "evolution_pressure":
                pressure,

            "confidence":
                confidence,

            "early_warning":
                early_warning,

            "status":
                "CRITICAL_TRANSITION_ACTIVE"

        }



    def analyze(
        self,
        metrics,
        prediction,
        transition
    ):

        return self.detect(
            metrics,
            prediction,
            transition
        )
