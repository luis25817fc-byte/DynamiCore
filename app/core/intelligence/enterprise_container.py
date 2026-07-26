from typing import Any, Dict, Type


class EnterpriseContainer:
    """
    DLIS-066A.3

    Enterprise Dependency Injection Container
    """

    VERSION = "2.0"

    def __init__(self):
        self._services: Dict[Type, Any] = {}

    def register(self, contract: Type, implementation: Any):
        self._services[contract] = implementation

    def resolve(self, contract: Type):

        if contract not in self._services:
            raise KeyError(
                f"Service not registered: {contract}"
            )

        return self._services[contract]

    def registered_services(self):

        return [
            c.__name__
            for c in self._services.keys()
        ]

    def diagnostics(self):

        return {

            "version": self.VERSION,

            "registered_services":
                len(self._services),

            "contracts":
                self.registered_services()

        }