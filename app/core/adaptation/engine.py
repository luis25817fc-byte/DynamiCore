
from .policy import PolicyEngine
from .calibration import CalibrationEngine
from .confidence import ConfidenceEngine
from .self_optimizer import SelfOptimizerEngine

from .adaptive_threshold import AdaptiveThresholdEngine
from .strategy_memory import StrategyMemory
from .adaptive_learning import AdaptiveLearningEngine
from .strategy_optimizer import StrategyOptimizer



class AdaptationEngine:


    def __init__(self):

        self.version = "6.0"

        self.total = 0

        self.successful = 0


        self.policy = PolicyEngine()

        self.calibration = CalibrationEngine()

        self.confidence = ConfidenceEngine()

        self.optimizer = SelfOptimizerEngine()


        # V6 INTELLIGENCE

        self.threshold = AdaptiveThresholdEngine()

        self.memory = StrategyMemory()

        self.learning = AdaptiveLearningEngine()

        self.strategy_optimizer = StrategyOptimizer()



    def adapt(

        self,

        feedback,

        decision=None,

        causal=None,

        state=None

    ):


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



        threshold = self.threshold.evaluate(

            confidence.get(
                "confidence",
                0
            ),

            feedback.get(
                "impact",
                0
            ),

            policy.get(
                "policy"
            )

        )



        memory = self.memory.store(

            decision.get(
                "decision",
                "unknown"
            ),

            policy.get(
                "policy"
            ),

            feedback.get(
                "outcome",
                "unknown"
            ),

            feedback.get(
                "impact",
                0
            ),

            confidence.get(
                "confidence",
                0
            )

        )



        learning = self.learning.analyze(

            self.memory.all()

        )



        strategy = self.strategy_optimizer.optimize(

            learning

        )



        optimization = self.optimizer.optimize(

            feedback,

            decision,

            confidence

        )



        return {


            "version":

                self.version,


            "confidence":

                confidence,


            "calibration":

                calibration,


            "policy":

                policy,


            "threshold":

                threshold,


            "memory":

                memory,


            "learning":

                learning,


            "strategy":

                strategy,


            "optimization":

                optimization

        }
