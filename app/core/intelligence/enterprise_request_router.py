from datetime import datetime, timezone
import uuid


class EnterpriseRequestRouter:

    VERSION = "1.0"


    def __init__(self):

        self.contracts = {}
        self.requests = []


    def register_contract(
        self,
        operation,
        required_fields
    ):

        contract = {
            "contract_id": str(uuid.uuid4()),
            "operation": operation,
            "required_fields": required_fields,
            "created": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }

        self.contracts[operation] = contract

        return contract


    def route(
        self,
        operation,
        payload
    ):

        request_id = str(uuid.uuid4())


        if operation not in self.contracts:

            result = {
                "request_id": request_id,
                "operation": operation,
                "status": "REJECTED",
                "reason": "UNKNOWN_OPERATION"
            }

            self.requests.append(result)

            return result


        contract = self.contracts[operation]


        missing = [
            field
            for field in contract["required_fields"]
            if field not in payload
        ]


        if missing:

            result = {
                "request_id": request_id,
                "operation": operation,
                "status": "REJECTED",
                "reason": "MISSING_FIELDS",
                "missing": missing
            }

            self.requests.append(result)

            return result


        result = {
            "request_id": request_id,
            "operation": operation,
            "status": "ACCEPTED",
            "contract": contract["contract_id"],
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }


        self.requests.append(result)

        return result


    def history(self):

        return self.requests


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "contracts": len(self.contracts),
            "requests": len(self.requests),
            "status": "READY"
        }