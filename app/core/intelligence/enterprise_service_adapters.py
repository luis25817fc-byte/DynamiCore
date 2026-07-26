from datetime import datetime, timezone


class EnterpriseServiceAdapter:

    """
    DLIS-066B.1

    Adapter base para integrar
    servicios existentes de DynamiCore
    con Enterprise Runtime.
    """

    VERSION = "2.0"


    def __init__(
        self,
        service_name,
        service_instance
    ):

        self.service_name = service_name

        self.service = service_instance


    def health(self):

        return {

            "service":
                self.service_name,

            "available":
                self.service is not None,

            "version":
                self.VERSION

        }


    def execute(
        self,
        method,
        *args,
        **kwargs
    ):

        if not hasattr(
            self.service,
            method
        ):

            raise AttributeError(

                f"{self.service_name} "
                f"does not implement {method}"

            )


        function = getattr(
            self.service,
            method
        )


        result = function(
            *args,
            **kwargs
        )


        return {

            "service":
                self.service_name,

            "method":
                method,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "result":
                result,

            "version":
                self.VERSION

        }


class DigitalTwinAdapter(
    EnterpriseServiceAdapter
):

    def __init__(
        self,
        twin
    ):

        super().__init__(
            "DIGITAL_TWIN",
            twin
        )


class CausalEngineAdapter(
    EnterpriseServiceAdapter
):

    def __init__(
        self,
        engine
    ):

        super().__init__(
            "CAUSAL_ENGINE",
            engine
        )


class DecisionEngineAdapter(
    EnterpriseServiceAdapter
):

    def __init__(
        self,
        engine
    ):

        super().__init__(
            "DECISION_ENGINE",
            engine
        )