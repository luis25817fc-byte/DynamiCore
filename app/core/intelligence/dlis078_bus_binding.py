
"""
DLIS-078-A002

Enterprise Intelligence Bus Binding

Responsibility:
- Register Enterprise Intelligence Bus
- Connect to Enterprise Service Registry
- No business logic changes
"""

from app.core.intelligence.enterprise_service_registry import (
    enterprise_service_registry
)


VERSION = "DLIS-078-A002"


class EnterpriseBusBinding:

    def __init__(
        self,
        bus=None
    ):

        self.bus = bus


    def register(self):

        if self.bus is None:

            raise ValueError(
                "Enterprise Intelligence Bus instance required"
            )


        return enterprise_service_registry.register(
            "enterprise_intelligence_bus",
            self.bus
        )


    def health(self):

        return {
            "status": "healthy",
            "binding": VERSION
        }


def create_bus_binding(bus):

    return EnterpriseBusBinding(
        bus
    )
