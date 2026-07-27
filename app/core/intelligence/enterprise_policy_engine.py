from datetime import datetime, timezone
import uuid


class EnterprisePolicyEngine:

    VERSION = "1.0"


    def __init__(self):

        self.rules = []
        self.enforcements = []


    def register_rule(
        self,
        name,
        action,
        required_role,
        risk_level="NORMAL"
    ):

        rule = {
            "rule_id": str(uuid.uuid4()),
            "name": name,
            "action": action,
            "required_role": required_role,
            "risk_level": risk_level,
            "created": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }

        self.rules.append(rule)

        return rule


    def enforce(
        self,
        identity,
        action
    ):

        matching_rules = [
            r for r in self.rules
            if r["action"] == action
        ]

        if not matching_rules:

            result = "NO_POLICY"


        else:

            rule = matching_rules[0]

            result = (
                "ALLOW"
                if identity.get("role")
                == rule["required_role"]
                else
                "BLOCK"
            )


        enforcement = {
            "enforcement_id": str(uuid.uuid4()),
            "identity": identity.get("name"),
            "action": action,
            "result": result,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }

        self.enforcements.append(enforcement)

        return enforcement


    def history(self):

        return self.enforcements


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "rules": len(self.rules),
            "enforcements": len(self.enforcements),
            "status": "READY"
        }