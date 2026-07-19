
class EvolutionDiffEngine:


    def __init__(self):

        self.version = "6.1.1"



    def _extract_metrics(self, snapshot):

        snapshot = snapshot or {}

        return {

            "risk":
                snapshot.get("risk", {})
                .get("risk_score", 0),


            "confidence":
                snapshot.get("validation", {})
                .get("confidence", 0),


            "coherence":
                snapshot.get("R(k)", {})
                .get("coherence", 0),


            "entropy":
                snapshot.get("H(k)", {})
                .get("shannon", 0),


            "divergence":
                snapshot.get("D(k)", {})
                .get("D(k)", 0),


            "regime":
                snapshot.get("regime", "unknown"),


            "policy":
                snapshot.get("adaptation", {})
                .get("policy", {})
                .get("policy", "unknown")

        }



    def compare(self, previous, current):

        old = self._extract_metrics(previous)

        new = self._extract_metrics(current)


        changes = {}


        for key in old:

            if old[key] != new[key]:

                changes[key] = {

                    "previous": old[key],

                    "current": new[key]

                }



        risk_change = new["risk"] - old["risk"]

        confidence_change = (
            new["confidence"]
            -
            old["confidence"]
        )


        if risk_change < 0:

            trajectory = "improving"

        elif risk_change > 0:

            trajectory = "degrading"

        else:

            trajectory = "stable"



        return {

            "version": self.version,

            "changed": bool(changes),

            "metrics": {

                "risk_change": risk_change,

                "confidence_change": confidence_change

            },

            "changes": changes,

            "trajectory": trajectory

        }
