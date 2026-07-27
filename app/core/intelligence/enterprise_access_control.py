from datetime import datetime, timezone
import uuid


class EnterpriseAccessControl:

    VERSION = "1.0"


    def __init__(self):

        self.policies = []
        self.decisions = []


    def create_policy(
        self,
        role,
        permissions
    ):

        policy = {
            "policy_id": str(uuid.uuid4()),
            "role": role,
            "permissions": permissions,
            "created": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }

        self.policies.append(policy)

        return policy


    def authorize(
        self,
        identity,
        action
    ):

        allowed = action in identity.get(
            "permissions",
            []
        )

        decision = {
            "decision_id": str(uuid.uuid4()),
            "identity": identity.get("name"),
            "action": action,
            "allowed": allowed,
            "result": "ALLOW" if allowed else "DENY",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }

        self.decisions.append(decision)

        return decision


    def history(self):

        return self.decisions


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "policies": len(self.policies),
            "decisions": len(self.decisions),
            "status": "READY"
        }