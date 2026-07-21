from datetime import datetime, timezone


class ReasoningEngine:
    """
    DynamiCore Reasoning Engine
    V8.0
    """

    VERSION = "V8.0"


    def reason(self, context):

        tensor = context.get("tensor", {})
        validation = context.get("validation", {})

        psi = tensor.get("tensor", {}).get("psi", 0)
        pressure = tensor.get("tensor", {}).get("pressure", 0)
        omega = tensor.get("tensor", {}).get("omega", 0)

        hypotheses = []

        if psi > 2:
            hypotheses.append("HIGH_POTENTIAL")

        if pressure > 0.5:
            hypotheses.append("STRUCTURAL_STABILITY")

        if omega > 0.7:
            hypotheses.append("HIGH_COHERENCE")

        global_validation = (
            validation.get("validation", {})
            .get("global_validation", False)
        )

        if global_validation:
            hypotheses.append("VALIDATED_STATE")
        else:
            hypotheses.append("UNSTABLE_STATE")

        return {

            "version": self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "hypotheses":
                hypotheses,

            "score":
                len(hypotheses)

        }
