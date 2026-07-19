
from datetime import datetime


class StructuralTimelineEngineV752:

    VERSION = "7.5.2"


    def build(self, states):

        timeline = []

        previous = None

        for index, state in enumerate(states):

            entropy = state.get("entropy", 0.0)
            health = state.get("structural_health", 0.0)
            risk = state.get("transition_risk", 0.0)

            delta_entropy = 0.0 if previous is None else entropy - previous["entropy"]
            delta_health = 0.0 if previous is None else health - previous["health"]

            timeline.append({

                "step": index,

                "timestamp": state.get("timestamp"),

                "entropy": entropy,

                "health": health,

                "risk": risk,

                "delta_entropy": round(delta_entropy, 6),

                "delta_health": round(delta_health, 6)

            })

            previous = {

                "entropy": entropy,

                "health": health

            }

        return timeline


    def summary(self, timeline):

        return {

            "version": self.VERSION,

            "states": len(timeline),

            "first": timeline[0] if timeline else None,

            "last": timeline[-1] if timeline else None,

            "generated": str(datetime.utcnow()),

            "status": "ONLINE"

        }


    def status(self):

        return {

            "version": self.VERSION,

            "module": "StructuralTimelineEngineV752",

            "status": "ONLINE"

        }
