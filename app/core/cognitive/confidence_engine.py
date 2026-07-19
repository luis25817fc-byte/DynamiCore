from datetime import datetime, timezone


class ConfidenceEngine:
    """
    DynamiCore Confidence Engine
    V8.0
    """

    VERSION = "V8.0"


    def evaluate(self, reasoning):

        hypotheses = reasoning.get(
            "hypotheses",
            []
        )

        score = reasoning.get(
            "score",
            0
        )

        confidence = min(
            1.0,
            score / 4.0
        )

        return {

            "version":
                self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "confidence":
                confidence,

            "accepted":
                confidence >= 0.75,

            "hypotheses":
                hypotheses

        }
