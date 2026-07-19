class DLISTensorBinding:

    VERSION = "DLIS-017"


    def build(self, engine_output):


        state = engine_output.get(
            "state_vector",
            {}
        )


        return {

            "psi":
                engine_output.get(
                    "potential",
                    state.get(
                        "potential",
                        0
                    )
                ),


            "pressure":
                engine_output.get(
                    "coherence",
                    state.get(
                        "coherence",
                        0
                    )
                ),


            "omega":
                state.get(
                    "coherence",
                    0
                ),


            "energy":
                engine_output.get(
                    "energy",
                    0
                ),


            "curvature":
                engine_output.get(
                    "divergence",
                    0
                ),


            "collapse":
                engine_output.get(
                    "risk",
                    0
                )
        }
