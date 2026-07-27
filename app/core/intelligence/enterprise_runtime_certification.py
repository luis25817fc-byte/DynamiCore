from datetime import datetime, timezone
import uuid
import time


class EnterpriseRuntimeCertification:

    VERSION = "1.0"

    def __init__(
        self,
        runtime,
        task_manager,
        scheduler,
        resource_monitor
    ):

        self.runtime = runtime
        self.task_manager = task_manager
        self.scheduler = scheduler
        self.resource_monitor = resource_monitor
        self.history = []


    def certify(self, iterations=100):

        certificate = {
            "certificate_id": str(uuid.uuid4()),
            "version": self.VERSION,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        start = time.perf_counter()

        executions = 0
        failures = 0

        runtime_ids = set()

        for i in range(iterations):

            try:

                result = self.runtime.execute(
                    "ENTERPRISE_CERTIFICATION_TEST",
                    {
                        "iteration": i,
                        "mode": "CERTIFICATION"
                    },
                    "HIGH"
                )

                executions += 1

                execution_id = result.get(
                    "execution_id"
                )

                if execution_id in runtime_ids:
                    raise Exception(
                        "DUPLICATE_EXECUTION_ID"
                    )

                runtime_ids.add(execution_id)


            except Exception:

                failures += 1


        task_records = len(
            self.task_manager.history()
        )

        scheduler_records = len(
            self.scheduler.history()
        )

        resource_records = len(
            self.resource_monitor.history()
        )

        runtime_records = len(
            self.runtime.history()
        )


        integrity = (
            task_records ==
            scheduler_records ==
            resource_records ==
            runtime_records
        )


        elapsed = time.perf_counter() - start


        success_rate = (
            executions / iterations
            if iterations
            else 0
        )


        passed = (
            failures == 0
            and integrity
            and success_rate == 1.0
        )


        certificate.update(
            {
                "iterations": iterations,
                "executions": executions,
                "failures": failures,
                "success_rate": success_rate,
                "history_integrity": integrity,
                "task_records": task_records,
                "scheduler_records": scheduler_records,
                "resource_records": resource_records,
                "runtime_records": runtime_records,
                "elapsed_seconds": elapsed,
                "status":
                    "ENTERPRISE_CERTIFIED"
                    if passed
                    else "FAILED"
            }
        )


        self.history.append(
            certificate
        )

        return certificate


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "certifications": len(
                self.history
            ),
            "status": "READY"
        }


    def certification_history(self):

        return self.history