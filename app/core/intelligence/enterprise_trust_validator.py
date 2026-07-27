from datetime import datetime, timezone
import uuid


class EnterpriseTrustValidator:

    VERSION = "1.0"


    def __init__(
        self,
        audit=None
    ):

        self.audit = audit
        self.validations = []


    def validate(
        self,
        security_result
    ):

        if security_result.get("result") == "ALLOW":

            trust_level = "HIGH"
            confidence = 0.95

        else:

            trust_level = "LOW"
            confidence = 0.10


        validation = {
            "trust_id": str(uuid.uuid4()),
            "request_id": security_result.get(
                "request_id"
            ),
            "identity": security_result.get(
                "identity",
                "UNKNOWN"
            ),
            "action": security_result.get(
                "action"
            ),
            "trust_level": trust_level,
            "confidence": confidence,
            "status": "VALIDATED",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }


        self.validations.append(validation)


        if self.audit:

            self.audit.record_response(
                security_result.get(
                    "request_id"
                ),
                validation
            )


        return validation


    def history(self):

        return self.validations


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "validations": len(
                self.validations
            ),
            "status": "READY"
        }