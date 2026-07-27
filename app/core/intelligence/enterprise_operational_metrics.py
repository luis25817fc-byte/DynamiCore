from datetime import datetime, timezone
import uuid


class EnterpriseOperationalMetrics:
    """
    DLIS-068.2

    Enterprise Operational Metrics Engine

    Analiza métricas operacionales
    y genera señales de desempeño.
    """

    VERSION = "2.0"


    def __init__(self):

        self.metrics = []
        self.analysis = []



    def register_metric(
        self,
        name,
        value
    ):

        metric = {

            "metric_id":
                str(uuid.uuid4()),

            "name":
                name,

            "value":
                value,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        self.metrics.append(metric)

        return metric



    def calculate_operational_score(self):

        if not self.metrics:

            return {

                "score": 0,

                "status":
                    "NO_DATA"

            }


        values = [

            metric["value"]

            for metric in self.metrics

        ]


        score = sum(values) / len(values)


        if score >= 0.85:

            status = "EXCELLENT"

        elif score >= 0.60:

            status = "STABLE"

        else:

            status = "DEGRADED"



        result = {

            "analysis_id":
                str(uuid.uuid4()),

            "operational_score":
                round(score, 3),

            "status":
                status,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        self.analysis.append(result)


        return result



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "metrics":
                len(self.metrics),

            "analyses":
                len(self.analysis),

            "status":
                "READY"

        }