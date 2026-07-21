

class IntelligenceVectorAdapter:


    VERSION = "DLIS-054-ADAPTER"


    def convert(self, report):

        if isinstance(report, dict):
            return report


        return {

            "reasoning": {

                "risk_level":
                    getattr(
                        report.prediction,
                        "risk_level",
                        "UNKNOWN"
                    ),

                "confidence":
                    getattr(
                        report.prediction,
                        "confidence",
                        0
                    )

            },


            "decision": {

                "action":
                    getattr(
                        report.decision,
                        "action",
                        "UNKNOWN"
                    )

            },


            "metrics":
                getattr(
                    report.state,
                    "metrics",
                    {}

                )

        }
