from datetime import datetime, timezone
import uuid


class EnterpriseOperationalForecast:
    """
    DLIS-068.4

    Enterprise Operational Forecast Engine

    Predicción básica de tendencias
    operacionales.
    """

    VERSION = "2.0"


    def __init__(self):

        self.forecasts = []



    def forecast(
        self,
        metric_name,
        values
    ):

        if len(values) < 2:

            trend = "INSUFFICIENT_DATA"

            risk = "UNKNOWN"

            recommendation = "COLLECT_MORE_DATA"


        else:

            difference = values[-1] - values[0]


            if difference < -0.10:

                trend = "DECLINING"

                risk = "HIGH"

                recommendation = "PREVENTIVE_OPTIMIZATION"


            elif difference < 0:

                trend = "SLIGHT_DECLINE"

                risk = "MEDIUM"

                recommendation = "MONITOR_SYSTEM"


            else:

                trend = "STABLE"

                risk = "LOW"

                recommendation = "CONTINUE_OPERATION"



        result = {

            "forecast_id":
                str(uuid.uuid4()),

            "metric":
                metric_name,

            "historical_values":
                values,

            "trend":
                trend,

            "risk":
                risk,

            "recommendation":
                recommendation,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        self.forecasts.append(result)

        return result



    def history(self):

        return self.forecasts



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "forecasts":
                len(self.forecasts),

            "status":
                "READY"

        }