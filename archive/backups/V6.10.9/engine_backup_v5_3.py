
from .policy import PolicyEngine
from .calibration import CalibrationEngine
from .confidence import ConfidenceEngine
from .self_optimizer import SelfOptimizerEngine


class AdaptationEngine:


    def __init__(self):

        self.version = "5.2"

        self.total = 0

        self.successful = 0


        self.policy = PolicyEngine()

        self.calibration = CalibrationEngine()

        self.confidence = ConfidenceEngine()

        self.optimizer = SelfOptimizerEngine()



    def adapt(

        self,

        feedback,

        decision=None,

        causal=None,

        state=None

    ):


        if not feedback:

            return {

                "adapted": False,

                "reason": "no_feedback"

            }



        decision = decision or {}

        causal = causal or {}



        confidence = self.confidence.evaluate(

            decision,

            causal,

            feedback

        )



        calibration = self.calibration.calibrate(

            decision,

            feedback

        )



        policy = self.policy.evaluate(

            feedback

        )



        optimization = self.optimizer.optimize(

            feedback,

            decision,

            confidence

        )



        if not feedback.get(

            "learn",

            False

        ):


            return {

                "adapted": False,

                "reason":

                    "learning_not_required",


                "confidence":

                    confidence,


                "calibration":

                    calibration,


                "policy":

                    policy,


                "optimization":

                    optimization

            }



        self.total += 1



        outcome = feedback.get(

            "outcome",

            "unknown"

        )



        if outcome == "successful":

            self.successful += 1



        return {


            "adapted": True,


            "version":

                self.version,


            "outcome":

                outcome,


            "confidence":

                confidence,


            "calibration":

                calibration,


            "policy":

                policy,


            "optimization":

                optimization,


            "success_rate":

                round(

                    self.successful /

                    self.total,

                    3

                )

        }
