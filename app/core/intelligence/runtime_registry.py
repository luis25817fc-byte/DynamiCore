from app.core.enterprise.registry_core import RegistryCore


class RuntimeRegistry(RegistryCore):

    VERSION = "7.1"


    def health(self):

        return {

            "version":
                self.VERSION,

            "modules":
                self.modules,

            "status":
                "ONLINE"
        }


runtime_registry = RuntimeRegistry()
