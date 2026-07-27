from datetime import datetime, timezone
import uuid


class EnterpriseSecurityGateway:

    VERSION = "1.0"


    def __init__(
        self,
        identity_manager=None,
        access_control=None,
        policy_engine=None,
        audit=None
    ):

        self.identity_manager = identity_manager
        self.access_control = access_control
        self.policy_engine = policy_engine
        self.audit = audit

        self.requests = []


    def authorize_request(
        self,
        identity_id,
        action
    ):

        request_id = str(uuid.uuid4())


        identity_result = (
            self.identity_manager.authenticate(identity_id)
            if self.identity_manager
            else {
                "authenticated": False
            }
        )


        if not identity_result.get(
            "authenticated",
            False
        ):

            result = {
                "request_id": request_id,
                "action": action,
                "result": "DENY",
                "reason": "INVALID_IDENTITY"
            }

            self.requests.append(result)

            return result


        identity = identity_result["identity"]


        if self.access_control:

            access = self.access_control.authorize(
                identity,
                action
            )

            if access["result"] != "ALLOW":

                result = {
                    "request_id": request_id,
                    "action": action,
                    "result": "DENY",
                    "reason": "ACCESS_CONTROL"
                }

                self.requests.append(result)

                return result


        if self.policy_engine:

            policy = self.policy_engine.enforce(
                identity,
                action
            )

            if policy["result"] != "ALLOW":

                result = {
                    "request_id": request_id,
                    "action": action,
                    "result": "DENY",
                    "reason": "POLICY_BLOCK"
                }

                self.requests.append(result)

                return result


        result = {
            "request_id": request_id,
            "identity": identity["name"],
            "action": action,
            "result": "ALLOW",
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
            "requests": len(self.requests),
            "status": "READY"
        }