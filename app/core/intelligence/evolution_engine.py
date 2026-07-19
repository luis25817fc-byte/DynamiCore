
from datetime import datetime

from app.core.intelligence.evolution_contract import EvolutionReport


class EvolutionEngine:

    version = "7.2"


    def analyze(
        self,
        system_id,
        previous_state,
        current_state
    ):

        delta = self._compute_delta(
            previous_state,
            current_state
        )


        transition = self._classify_transition(
            delta
        )


        confidence = self._confidence(
            delta
        )


        return EvolutionReport(

            system_id=system_id,

            timestamp=datetime.utcnow(),

            previous_state=previous_state,

            current_state=current_state,

            delta=delta,

            transition=transition,

            confidence=confidence
        )


    def _compute_delta(
        self,
        previous,
        current
    ):

        delta = {}

        keys = set(
            previous.keys()
        ).union(
            current.keys()
        )


        for key in keys:

            old = previous.get(
                key,
                0
            )

            new = current.get(
                key,
                0
            )

            if isinstance(old,(int,float)) and isinstance(new,(int,float)):

                delta[f"{key}_delta"] = new - old


        return delta



    def _classify_transition(
        self,
        delta
    ):

        growth = any(
            value > 0
            for value in delta.values()
        )


        decline = any(
            value < 0
            for value in delta.values()
        )


        if growth and not decline:
            return "STRUCTURAL_GROWTH"


        if decline and not growth:
            return "STRUCTURAL_DECAY"


        if growth and decline:
            return "STRUCTURAL_RECONFIGURATION"


        return "STABLE"



    def _confidence(
        self,
        delta
    ):

        magnitude = sum(
            abs(v)
            for v in delta.values()
        )


        if magnitude == 0:
            return 1.0


        return min(
            0.95,
            0.5 + magnitude / 100
        )
