
class ValidationEngine:


    def validate(self, state):

        errors = []


        if state.entropy < 0:
            errors.append(
                "entropy_negative"
            )


        if state.coherence < 0 or state.coherence > 1:
            errors.append(
                "coherence_out_of_range"
            )


        if state.potential < 0:
            errors.append(
                "negative_potential"
            )


        if state.divergence < 0:
            errors.append(
                "negative_divergence"
            )


        confidence = 1.0


        if errors:
            confidence -= (
                len(errors) * 0.25
            )


        return {

            "valid": len(errors) == 0,

            "errors": errors,

            "confidence": max(
                confidence,
                0
            )
        }
