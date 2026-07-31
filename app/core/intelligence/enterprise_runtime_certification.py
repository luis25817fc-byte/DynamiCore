
from datetime import datetime, timezone
import time
import uuid


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

        start = time.perf_counter()

        certificate = {
            "certificate_id": str(uuid.uuid4()),
            "version": self.VERSION,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "iterations": iterations
        }

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

                execution_id = result.get(
                    "execution_id"
                )

                if execution_id:

                    if execution_id in runtime_ids:
                        raise Exception(
                            "DUPLICATE_EXECUTION_ID"
                        )

                    runtime_ids.add(
                        execution_id
                    )

                executions += 1


            except Exception:

                failures += 1



        def get_history(obj):

            value = getattr(
                obj,
                "history",
                []
            )

            if callable(value):
                return value()

            return value



        task_records = len(
            get_history(
                self.task_manager
            )
        )

        scheduler_records = len(
            get_history(
                self.scheduler
            )
        )

        resource_records = len(
            get_history(
                self.resource_monitor
            )
        )

        runtime_records = len(
            get_history(
                self.runtime
            )
        )


        integrity = (
            task_records ==
            scheduler_records ==
            resource_records ==
            runtime_records
        )


        elapsed = (
            time.perf_counter()
            - start
        )


        passed = (
            failures == 0
            and integrity
        )


        certificate.update(
            {
                "executions": executions,
                "failures": failures,
                "task_records": task_records,
                "scheduler_records": scheduler_records,
                "resource_records": resource_records,
                "runtime_records": runtime_records,
                "history_integrity": integrity,
                "elapsed_seconds": elapsed,
                "errors": [],
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
            )
        }


    def certification_history(self):

        return self.history
