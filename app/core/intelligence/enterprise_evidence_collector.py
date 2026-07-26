from datetime import datetime, timezone
from uuid import uuid4


class EnterpriseEvidenceCollector:
    """
    DLIS-065.1

    Enterprise Evidence Collector

    Construye paquetes de evidencia
    auditables para la Causal Intelligence Layer.
    """

    VERSION = "1.0"

    def __init__(self):

        self.collection_count = 0
        self.history = []


    def collect(
        self,
        sources: dict,
        context: dict | None = None
    ):

        package = {

            "evidence_id":
                str(uuid4()),

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "sources":
                sources,

            "context":
                context or {},

            "source_count":
                len(sources),

            "validation":
                "VALID",

            "version":
                self.VERSION

        }

        self.collection_count += 1

        self.history.append(package)

        return package


    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "collections":
                self.collection_count,

            "history_size":
                len(self.history)

        }