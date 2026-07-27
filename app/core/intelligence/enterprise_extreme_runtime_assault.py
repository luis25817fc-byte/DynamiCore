from datetime import datetime, timezone
import uuid
import time
import random


class EnterpriseExtremeRuntimeAssault:

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


    def execute(
        self,
        operations=100000
    ):

        report = {
            "assault_id": str(uuid.uuid4()),
            "operations": operations,
            "completed": 0,
            "failed": 0,
            "recovered": 0,
            "latencies": [],
            "duplicate_ids": 0,
            "events": []
        }

        execution_ids = set()

        start = time.perf_counter()


        for i in range(operations):

            begin = time.perf_counter()

            priority = random.choice(
                [
                    "CRITICAL",
                    "HIGH",
                    "NORMAL",
                    "LOW"
                ]
            )

            try:

                # Fallos controlados simulados
                simulated_failure = (
                    i % 997 == 0
                    and i != 0
                )

                if simulated_failure:
                    raise RuntimeError(
                        "SIMULATED_RUNTIME_FAILURE"
                    )


                result = self.runtime.execute(
                    "EXTREME_ASSAULT_TEST",
                    {
                        "iteration": i,
                        "priority": priority,
                        "mode": "STRESS"
                    },
                    priority
                )


                execution_id = result.get(
                    "execution_id"
                )


                if execution_id in execution_ids:
                    report["duplicate_ids"] += 1


                execution_ids.add(
                    execution_id
                )


                report["completed"] += 1

                report["events"].append(
                    {
                        "iteration": i,
                        "status": "SUCCESS",
                        "execution_id": execution_id
                    }
                )


            except Exception as error:

                report["failed"] += 1

                # recuperación simulada
                try:

                    recovery = self.runtime.execute(
                        "RECOVERY_AFTER_FAILURE",
                        {
                            "failed_iteration": i
                        },
                        "HIGH"
                    )

                    report["recovered"] += 1

                    report["events"].append(
                        {
                            "iteration": i,
                            "status": "RECOVERED",
                            "reason": str(error),
                            "execution_id":
                                recovery.get(
                                    "execution_id"
                                )
                        }
                    )

                except Exception:

                    report["events"].append(
                        {
                            "iteration": i,
                            "status": "FAILED"
                        }
                    )


            report["latencies"].append(
                time.perf_counter() - begin
            )


        elapsed = time.perf_counter() - start


        histories = {
            "tasks": len(
                self.task_manager.history()
            ),
            "scheduler": len(
                self.scheduler.history()
            ),
            "resources": len(
                self.resource_monitor.history()
            ),
            "runtime": len(
                self.runtime.history()
            )
        }


        report["history_integrity"] = (
            len(set(histories.values())) == 1
        )


        report["success_rate"] = (
            report["completed"] /
            operations
        )


        report["elapsed_seconds"] = elapsed

        report["throughput"] = (
            operations / elapsed
            if elapsed > 0
            else 0
        )


        sorted_latency = sorted(
            report["latencies"]
        )

        report["p95_latency"] = sorted_latency[
            int(len(sorted_latency) * 0.95)
        ]

        report["p99_latency"] = sorted_latency[
            int(len(sorted_latency) * 0.99)
        ]


        report["histories"] = histories

        report["stability_score"] = (
            100
            if (
                report["history_integrity"]
                and report["duplicate_ids"] == 0
            )
            else 0
        )


        report["status"] = (
            "ENTERPRISE_STABLE"
            if report["stability_score"] == 100
            else "DEGRADED"
        )


        report["timestamp"] = datetime.now(
            timezone.utc
        ).isoformat()

        report["version"] = self.VERSION


        self.history.append(report)

        return report


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "tests": len(self.history),
            "status": "READY"
        }