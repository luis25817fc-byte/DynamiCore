
"""
DynamiCore Enterprise
DLIS-033
Cognitive Kernel Contract
"""

from datetime import datetime, timezone
from uuid import uuid4


class KernelStatus:

    def __init__(
        self,
        code=200,
        message="OK"
    ):

        self.code = code
        self.message = message
        self.trace_id = str(uuid4())
        self.timestamp = datetime.now(
            timezone.utc
        ).isoformat()


    def __repr__(self):

        return (
            f"KernelStatus("
            f"code={self.code}, "
            f"message='{self.message}', "
            f"trace_id='{self.trace_id}', "
            f"timestamp='{self.timestamp}')"
        )


class KernelInput:

    def __init__(
        self,
        objective,
        payload
    ):

        self.objective = objective
        self.payload = payload



class KernelOutput:

    def __init__(
        self,
        status,
        decision,
        state_delta,
        reasoning,
        confidence
    ):

        self.status = status
        self.decision = decision
        self.state_delta = state_delta
        self.reasoning = reasoning
        self.confidence = confidence

        self.rollback_required = (
            confidence < 0.5
        )


    def __repr__(self):

        return (
            f"KernelOutput("
            f"status={self.status}, "
            f"decision={self.decision}, "
            f"state_delta={self.state_delta}, "
            f"reasoning={self.reasoning}, "
            f"confidence={self.confidence}, "
            f"rollback_required={self.rollback_required})"
        )


class EnterpriseKernelContract:

    VERSION = "DLIS-033"


    def validate_output(
        self,
        output
    ):

        if output.confidence < 0.5:

            output.status = KernelStatus(
                500,
                "LOW_CONFIDENCE_REEVALUATION_REQUIRED"
            )

            output.rollback_required = True


        return output
