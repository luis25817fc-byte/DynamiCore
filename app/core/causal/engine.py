
from .graph import CausalGraph


class CausalEngine:


    def __init__(self):

        self.graph = CausalGraph()


        self.graph.add_relation(
            "coherence_drop",
            "system_instability",
            0.8
        )

        self.graph.add_relation(
            "divergence_growth",
            "risk_increase",
            0.7
        )

        self.graph.add_relation(
            "entropy_growth",
            "complexity_increase",
            0.6
        )


    def analyze(self, attribution):

        dominant = attribution.get(
            "dominant_factor",
            "unknown"
        )

        effects = self.graph.get_effects(
            dominant
        )

        confidence = attribution.get(
            "confidence",
            0
        )


        ranking = sorted(
            effects,
            key=lambda x: x["weight"],
            reverse=True
        )


        strength = sum(
            item["weight"]
            for item in effects
        )


        if strength > 0.7:
            level = "strong"

        elif strength > 0.3:
            level = "moderate"

        else:
            level = "weak"


        return {

            "cause": dominant,

            "effects": effects,

            "effect_ranking": ranking,

            "causal_strength": strength,

            "confidence": confidence,

            "level": level,

            "causal_found": len(effects) > 0

        }
