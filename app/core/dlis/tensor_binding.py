<<<<<<< HEAD


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
=======
class DLISTensorBinding:

    VERSION = "DLIS-017"


    def build(self, engine_output):


        state = engine_output.get(
            "state_vector",
            {}
>>>>>>> origin/validation-suite-v2
        )


        return {

<<<<<<< HEAD

            "psi":
                output
                .get(
                    "Ψ(k)",
                    {}
                )
                .get(
                    "Ψ(k)",
                    0
=======
            "psi":
                engine_output.get(
                    "potential",
                    state.get(
                        "potential",
                        0
                    )
>>>>>>> origin/validation-suite-v2
                ),


            "pressure":
<<<<<<< HEAD
                output
                .get(
                    "R(k)",
                    {}
                )
                .get(
                    "R(k)",
                    0
=======
                engine_output.get(
                    "coherence",
                    state.get(
                        "coherence",
                        0
                    )
>>>>>>> origin/validation-suite-v2
                ),


            "omega":
<<<<<<< HEAD
                output
                .get(
                    "R(k)",
                    {}
                )
                .get(
=======
                state.get(
>>>>>>> origin/validation-suite-v2
                    "coherence",
                    0
                ),


            "energy":
<<<<<<< HEAD
                output
                .get(
                    "Ψ(k)",
                    {}
                )
                .get(
=======
                engine_output.get(
>>>>>>> origin/validation-suite-v2
                    "energy",
                    0
                ),


            "curvature":
<<<<<<< HEAD
                output
                .get(
                    "D(k)",
                    {}
                )
                .get(
                    "D(k)",
=======
                engine_output.get(
                    "divergence",
>>>>>>> origin/validation-suite-v2
                    0
                ),


            "collapse":
<<<<<<< HEAD
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

=======
                engine_output.get(
                    "risk",
                    0
                )
        }
>>>>>>> origin/validation-suite-v2
