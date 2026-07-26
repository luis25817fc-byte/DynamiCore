from datetime import datetime, timezone
from uuid import uuid4


class EnterpriseStateDivergenceAnalyzer:
    """
    DLIS-066.3

    Enterprise State Divergence Analyzer
    """

    VERSION = "1.0"


    def __init__(self):

        self.analyses = 0

        self.history = []


    def analyze(
        self,
        expected_state: dict,
        actual_state: dict
    ):

        divergences = {}

        for key, expected in expected_state.items():

            if key not in actual_state:
                continue

            actual = actual_state[key]

            if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):

                divergences[key] = round(
                    actual - expected,
                    4
                )

            elif expected != actual:

                divergences[key] = {
                    "expected": expected,
                    "actual": actual
                }

        impact = sum(
            abs(v)
            for v in divergences.values()
            if isinstance(v, (int, float))
        )

        if impact >= 0.25:
            severity = "HIGH"
        elif impact >= 0.10:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        result = {

            "analysis_id":
                str(uuid4()),

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "severity":
                severity,

            "impact_score":
                round(impact, 4),

            "divergence_count":
                len(divergences),

            "divergences":
                divergences,

            "version":
                self.VERSION

        }

        self.analyses += 1

        self.history.append(result)

        return result


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "analyses":
                self.analyses,

            "history_size":
                len(self.history)

        }