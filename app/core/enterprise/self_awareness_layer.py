
from app.core.enterprise.observability import EnterpriseObservability
from app.core.enterprise.monitoring_alert import EnterpriseMonitoringAlert
from app.core.enterprise.global_state_manager import EnterpriseGlobalStateManager
from app.core.enterprise.runtime_state import EnterpriseRuntimeState
from app.core.enterprise.runtime_manager import EnterpriseRuntimeManager


class SelfAwarenessLayer:

    VERSION = "6.9.6"

    def __init__(self):
        self.observability = EnterpriseObservability()
        self.monitoring = EnterpriseMonitoringAlert()
        self.global_state = EnterpriseGlobalStateManager()
        self.runtime_state = EnterpriseRuntimeState()
        self.runtime = EnterpriseRuntimeManager()

    def process(self, component, data, state):

        self.runtime_state.update()

        self.global_state.update(component, data)

        self.observability.record_event()

        heartbeat = self.runtime.heartbeat()

        # Adaptador objeto -> dict
        monitor_state = (
            state if isinstance(state, dict)
            else vars(state)
        )

        alert = self.monitoring.analyze(
            monitor_state
        )

        return {
            "version": self.VERSION,
            "status": "SELF_AWARENESS_ACTIVE",
            "heartbeat": heartbeat,
            "global_state": self.global_state.snapshot(),
            "runtime_state": self.runtime_state.__dict__,
            "observability": self.observability.snapshot(),
            "alert": alert
        }
