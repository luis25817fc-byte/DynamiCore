

class DLISTensorBinding:


    VERSION = "DLIS-017"



    def build(
        self,
        engine_output
    ):


        output = (
            engine_output
            .get(
                "output",
                {}
            )
        )


        return {


            "psi":
                output
                .get(
                    "Ψ(k)",
                    {}
                )
                .get(
                    "Ψ(k)",
                    0
                ),


            "pressure":
                output
                .get(
                    "R(k)",
                    {}
                )
                .get(
                    "R(k)",
                    0
                ),


            "omega":
                output
                .get(
                    "R(k)",
                    {}
                )
                .get(
                    "coherence",
                    0
                ),


            "energy":
                output
                .get(
                    "Ψ(k)",
                    {}
                )
                .get(
                    "energy",
                    0
                ),


            "curvature":
                output
                .get(
                    "D(k)",
                    {}
                )
                .get(
                    "D(k)",
                    0
                ),


            "collapse":
                output
                .get(
                    "risk",
                    {}
                )
                .get(
                    "risk_score",
                    0
                )

        }

