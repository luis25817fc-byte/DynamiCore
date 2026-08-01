from .context_builder import ContextBuilder
from .reasoning_engine import ReasoningEngine
from .confidence_engine import ConfidenceEngine
from .objective_manager import ObjectiveManager
from .action_selector import ActionSelector
from .feedback_integrator import FeedbackIntegrator


class CognitiveRegistry:
    """
    DynamiCore Cognitive Registry
    V8.0
    """

    VERSION = "V8.0"


    def build(self):

        return {

            "context_builder":
                ContextBuilder(),

            "reasoning_engine":
                ReasoningEngine(),

            "confidence_engine":
                ConfidenceEngine(),

            "objective_manager":
                ObjectiveManager(),

            "action_selector":
                ActionSelector(),

            "feedback_integrator":
                FeedbackIntegrator()

        }
