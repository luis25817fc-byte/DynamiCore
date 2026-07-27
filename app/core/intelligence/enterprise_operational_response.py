from datetime import datetime, timezone
import uuid


class EnterpriseOperationalResponse:
    """
    DLIS-068.5

    Enterprise Operational Response Engine

    Genera respuestas operacionales
    basadas en alertas y predicciones.
    """

    VERSION = "2.0"


    def __init__(self):

        self.responses = []



    def generate_response(
        self,
        alert,
        forecast
    ):

        if (
            alert.get("status") == "ALERT"
            and forecast.get("risk") == "HIGH"
        ):

            action = "EXECUTE_PREVENTIVE_OPTIMIZATION"

            priority = "HIGH"


        elif (
            alert.get("status") == "ALERT"
        ):

            action = "MONITOR_AND_ANALYZE"

            priority = "MEDIUM"


        else:

            action = "CONTINUE_OPERATION"

            priority = "LOW"



        response = {

            "response_id":
                str(uuid.uuid4()),

            "action":
                action,

            "priority":
                priority,

            "alert_reference":
                alert.get("alert_id"),

            "forecast_reference":
                forecast.get("forecast_id"),

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        self.responses.append(response)

        return response



    def history(self):

        return self.responses



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "responses":
                len(self.responses),

            "status":
                "READY"

        }