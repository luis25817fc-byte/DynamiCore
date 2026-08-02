
from datetime import datetime, timezone


class RuntimeSupervisor:

    VERSION = "EOS-003"

    def __init__(self, process_manager):

        self.process_manager = process_manager

    def inspect(self):

        processes = self.process_manager.list()

        report = {}

        healthy = True

        for name, process in processes.items():

            state = process.get("status", "UNKNOWN")

            report[name] = state

            if state not in (
                "READY",
                "RUNNING"
            ):

                healthy = False

        return {

            "version": self.VERSION,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "healthy":
                healthy,

            "processes":
                len(processes),

            "report":
                report

        }
