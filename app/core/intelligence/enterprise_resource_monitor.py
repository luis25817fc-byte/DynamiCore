from datetime import datetime, timezone
import uuid


class EnterpriseResourceMonitor:

    VERSION = "1.0"


    def __init__(self):

        self.metrics = []


    def record_usage(
        self,
        task_id,
        cpu_load,
        memory_usage,
        active_tasks
    ):

        metric = {
            "metric_id": str(uuid.uuid4()),
            "task_id": task_id,
            "cpu_load": cpu_load,
            "memory_usage": memory_usage,
            "active_tasks": active_tasks,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }


        self.metrics.append(metric)

        return metric


    def latest(self):

        if not self.metrics:

            return {
                "status": "NO_DATA"
            }

        return self.metrics[-1]


    def history(self):

        return self.metrics


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "metrics": len(self.metrics),
            "status": "READY"
        }