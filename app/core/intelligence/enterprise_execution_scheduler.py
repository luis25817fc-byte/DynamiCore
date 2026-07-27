from datetime import datetime, timezone
import uuid


class EnterpriseExecutionScheduler:

    VERSION = "1.0"


    def __init__(self):

        self.queue = []
        self.history_records = []


    def submit_task(
        self,
        task_id,
        operation,
        priority="NORMAL"
    ):

        scheduled = {
            "schedule_id": str(uuid.uuid4()),
            "task_id": task_id,
            "operation": operation,
            "priority": priority,
            "status": "QUEUED",
            "created": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }

        self.queue.append(scheduled)

        return scheduled


    def next_task(self):

        if not self.queue:

            return {
                "status": "EMPTY"
            }


        self.queue.sort(
            key=lambda x: x["priority"]
        )


        task = self.queue.pop(0)

        task["status"] = "SCHEDULED"

        self.history_records.append(task)

        return task


    def queue_status(self):

        return self.queue


    def history(self):

        return self.history_records


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "queued_tasks": len(self.queue),
            "scheduled_tasks": len(self.history_records),
            "status": "READY"
        }