
from datetime import datetime, timezone


class DLISRuntimePipeline:

    """
    DLIS-013

    Runtime integration layer.

    Connects:
    DynamiCore Engine
    +
    DLIS Intelligence
    +
    Validation
    +
    Routing
    """

    VERSION = "DLIS-013"


    def __init__(
        self,
        engine=None,
        dlis_binding=None,
        validator=None
    ):

        self.engine = engine
        self.dlis_binding = dlis_binding
        self.validator = validator



    def run(
        self,
        system_state,
        dlis_tensor,
        fusion_state
    ):


        stages = {


            "engine":
                self.engine is not None,


            "dlis":
                dlis_tensor is not None
                and fusion_state is not None,


            "validation":
                False,


            "routing":
                False

        }



        validation_result = None


        if self.validator:


            validation_result = (
                self.validator.validate(
                    dlis_tensor,
                    fusion_state
                )
            )


            stages["validation"] = (
                validation_result.get(
                    "runtime_ready",
                    False
                )
            )


        routing = {

            "prediction":
                fusion_state.get(
                    "actions",
                    []
                ).count(
                    "PREDICT"
                ) > 0,


            "adaptation":
                fusion_state.get(
                    "actions",
                    []
                ).count(
                    "ADAPT"
                ) > 0,


            "decision":
                fusion_state.get(
                    "actions",
                    []
                ).count(
                    "DECIDE"
                ) > 0

        }


        stages["routing"] = any(
            routing.values()
        )


        return {


            "version":
                self.VERSION,


            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),


            "pipeline_status":
                (
                    "ONLINE"
                    if all(
                        stages.values()
                    )
                    else
                    "PARTIAL"
                ),


            "stages":
                stages,


            "routing":
                routing,


            "validation":
                validation_result,


            "decision_ready":
                stages["validation"]
                and stages["routing"]

        }
