
from .runtime_state import EnterpriseRuntimeState


class EnterpriseRuntimeManager:

    VERSION = "6.6.0"

    def __init__(self):
        self.state = EnterpriseRuntimeState()

    def heartbeat(self):

        return {
            "version": self.VERSION,
            "runtime": self.state.update()
        }
