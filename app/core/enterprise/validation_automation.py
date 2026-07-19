
import json
from datetime import datetime


class EnterpriseValidationAutomation:

    VERSION = "6.8.4"


    def __init__(
        self,
        bootstrap
    ):

        self.bootstrap = bootstrap


    def run(
        self,
        token="enterprise_validation_token",
        state=None
    ):

        state = state or {
            "risk": "LOW",
            "event": "VALIDATION_RUN"
        }


        system = self.bootstrap.build()


        result = system[
            "enterprise_core"
        ].start(
            token,
            state
        )


        validation = {

            "version": self.VERSION,

            "timestamp":
                str(datetime.utcnow()),

            "status":
                "PASSED"
                if result.get("status")
                == "ENTERPRISE_ACTIVE"
                else "FAILED",

            "checks": {

                "security":
                    result["security"]
                    ["authenticated"],

                "runtime":
                    result["system"]
                    ["runtime"]
                    ["runtime"]
                    ["status"]
                    == "ACTIVE",

                "decision":
                    result["system"]
                    ["decision"]
                    ["decision_status"]
                    == "GENERATED",

                "monitoring":
                    result["system"]
                    ["alert"]
                    ["monitoring"]
                    == "ACTIVE",

                "deployment":
                    result["deployment"]
                    ["deployment"]
                    == "READY"
            },

            "enterprise_result":
                result
        }


        return validation


    def export(
        self,
        report,
        path="enterprise_validation_report.json"
    ):

        with open(
            path,
            "w"
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                default=str
            )


        return {
            "version": self.VERSION,
            "exported": True,
            "file": path
        }
