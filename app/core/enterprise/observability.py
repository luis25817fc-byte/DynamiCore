
import time


class EnterpriseObservability:

    VERSION = "6.7.1"


    def __init__(self):

        self.metrics = {
            "events": 0,
            "errors": 0,
            "uptime": 0
        }

        self.start_time = time.time()


    def record_event(self):

        self.metrics["events"] += 1


    def record_error(self):

        self.metrics["errors"] += 1


    def snapshot(self):

        self.metrics["uptime"] = (
            time.time()
            -
            self.start_time
        )

        return {

            "version": self.VERSION,

            "status": "MONITORING",

            "metrics":
                self.metrics
        }
