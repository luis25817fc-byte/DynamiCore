from app.core.enterprise.registry_core import RegistryCore


class AutoRegistry(RegistryCore):

    VERSION = "7.1"


    def __init__(self, kernel=None):

        super().__init__()
        self.kernel = kernel


auto_registry = AutoRegistry()
