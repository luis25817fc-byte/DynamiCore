class DLISTensorBinding:

    VERSION = "DLIS-017"

    def build(self, engine_output):

        output = engine_output.get(
            "output",
            engine_output
        )

        state = engine_output.get(
            "state_vector",
            {}
        )

        return {
            "psi": output.get("Ψ(k)", {}).get(
                "Ψ(k)",
                engine_output.get("potential", state.get("potential", 0))
            ),

            "pressure": output.get("R(k)", {}).get(
                "R(k)",
                engine_output.get("coherence", state.get("coherence", 0))
            ),

            "omega": state.get(
                "coherence",
                0
            ),

            "energy": output.get(
                "energy",
                engine_output.get("energy", 0)
            ),

            "curvature": output.get("D(k)", {}).get(
                "D(k)",
                engine_output.get("divergence", 0)
            ),

            "collapse": output.get(
                "risk",
                engine_output.get("risk", 0)
            )
        }
