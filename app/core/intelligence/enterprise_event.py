from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

from .enterprise_event_types import EnterpriseEventType
from .enterprise_priority import normalize_priority


@dataclass
class EnterpriseEvent:
    """
    DLIS-055
    Enterprise Intelligence Event Contract
    """

    event_type: EnterpriseEventType

    source: str

    payload: dict

    target: str = None

    priority: int = 2

    metadata: dict = field(
        default_factory=dict
    )

    event_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    correlation_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    timestamp: str = field(
        default_factory=lambda:
        datetime.now(timezone.utc).isoformat()
    )

    status: str = "CREATED"


    def __post_init__(self):

        self.priority = normalize_priority(
            self.priority
        )

        if isinstance(self.event_type, str):

            self.event_type = EnterpriseEventType(
                self.event_type
            )


    def mark_processed(self):

        self.status = "PROCESSED"



    def mark_failed(self, reason):

        self.status = "FAILED"

        self.metadata["error"] = reason



    def to_dict(self):

        return {

            "event_id":
                self.event_id,

            "correlation_id":
                self.correlation_id,

            "event_type":
                self.event_type.value,

            "source":
                self.source,

            "target":
                self.target,

            "priority":
                self.priority.name,

            "timestamp":
                self.timestamp,

            "status":
                self.status,

            "payload":
                self.payload,

            "metadata":
                self.metadata

        }