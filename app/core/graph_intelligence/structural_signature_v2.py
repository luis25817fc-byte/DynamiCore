
"""
DynamiCore V6.11.0
Structural Signature Evolution Layer
"""


import hashlib
import json


class StructuralSignatureV2:

    VERSION = "6.11.0"


    def compare(
        self,
        previous,
        current
    ):

        previous = previous or {}

        current = current or {}


        keys = (
            set(previous.keys()) |
            set(current.keys())
        )


        changes = {}


        for key in keys:

            old = previous.get(key)

            new = current.get(key)


            if old != new:

                changes[key] = {

                    "previous": old,

                    "current": new

                }



        structural_shift = len(
            changes
        )


        previous_density = previous.get(
            "density",
            0
        )

        current_density = current.get(
            "density",
            0
        )


        density_delta = round(
            current_density -
            previous_density,
            4
        )



        previous_complexity = previous.get(
            "structural_complexity",
            0
        )

        current_complexity = current.get(
            "structural_complexity",
            0
        )


        complexity_delta = round(
            current_complexity -
            previous_complexity,
            4
        )



        evolution_pressure = round(
            abs(density_delta) +
            abs(complexity_delta) +
            structural_shift * 0.1,
            4
        )



        signature_payload = {

            "density_delta":
                density_delta,

            "complexity_delta":
                complexity_delta,

            "structural_shift":
                structural_shift

        }



        signature_hash = hashlib.sha256(
            json.dumps(
                signature_payload,
                sort_keys=True
            ).encode()
        ).hexdigest()



        if evolution_pressure >= 1:

            state = "CRITICAL_EVOLUTION"

        elif evolution_pressure >= 0.5:

            state = "ACTIVE_EVOLUTION"

        else:

            state = "STABLE_EVOLUTION"



        return {

            "version":
                self.VERSION,

            "changes":
                changes,

            "structural_shift":
                structural_shift,

            "density_delta":
                density_delta,

            "complexity_delta":
                complexity_delta,

            "evolution_pressure":
                evolution_pressure,

            "state":
                state,

            "signature_hash":
                signature_hash

        }
