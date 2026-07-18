
from datetime import datetime



class MemoryBindingAdapter:


    VERSION = "7.6.13"



    def __init__(
        self,
        memory_engine=None
    ):

        self.memory_engine = memory_engine



    def store_state(
        self,
        state
    ):

        if self.memory_engine:

            if hasattr(
                self.memory_engine,
                "push_state"
            ):

                return self.memory_engine.push_state(
                    state
                )


        return {

            "status":
                "MEMORY_ADAPTER_IDLE"

        }



    def latest(self):

        if self.memory_engine:

            if hasattr(
                self.memory_engine,
                "latest_state"
            ):

                return self.memory_engine.latest_state()


        return None





class PredictionBindingAdapter:


    VERSION = "7.6.13"



    def __init__(
        self,
        prediction_engine=None
    ):

        self.prediction_engine = prediction_engine



    def predict(
        self,
        context
    ):

        if self.prediction_engine:

            return self.prediction_engine.predict(
                context
            )


        return {

            "status":
                "PREDICTION_ADAPTER_IDLE"

        }





class DecisionBindingAdapter:


    VERSION = "7.6.13"



    def __init__(
        self,
        decision_engine=None
    ):

        self.decision_engine = decision_engine



    def decide(
        self,
        context
    ):

        if self.decision_engine:

            return self.decision_engine.decide(
                context
            )


        return {

            "status":
                "DECISION_ADAPTER_IDLE"

        }





class CanonicalBindingAdapter:


    VERSION = "7.6.13"



    def __init__(
        self,
        memory=None,
        prediction=None,
        decision=None
    ):

        self.created = datetime.utcnow()


        self.memory = MemoryBindingAdapter(
            memory
        )


        self.prediction = PredictionBindingAdapter(
            prediction
        )


        self.decision = DecisionBindingAdapter(
            decision
        )



    def status(self):

        return {

            "version":
                self.VERSION,

            "module":
                "CanonicalBindingAdapter",

            "memory":
                "CONNECTED",

            "prediction":
                "CONNECTED",

            "decision":
                "CONNECTED",

            "status":
                "ONLINE"

        }
