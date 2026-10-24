import unittest

from app.core.enterprise_os.event_bus import EventBus
from app.core.enterprise_os.process_manager import ProcessManager
from app.core.enterprise_os.runtime_supervisor import RuntimeSupervisor
from app.core.enterprise_os.scheduler import EnterpriseScheduler
from app.core.enterprise_os.resource_manager import EnterpriseResourceManager
from app.core.enterprise_os.health_monitor import EnterpriseHealthMonitor
from app.core.enterprise_os.lifecycle_manager import EnterpriseLifecycleManager
from app.core.enterprise_os.telemetry import EnterpriseTelemetry
from app.core.enterprise_os.enterprise_services import EnterpriseServices


class TestEnterpriseOSIntegration(unittest.TestCase):
    def test_cross_component_workflow(self):
        bus = EventBus()
        pm = ProcessManager()
        supervisor = RuntimeSupervisor(pm)
        resources = EnterpriseResourceManager()
        health = EnterpriseHealthMonitor(event_bus=bus)
        telemetry = EnterpriseTelemetry()
        lifecycle = EnterpriseLifecycleManager(
            process_manager=pm,
            runtime_supervisor=supervisor,
            event_bus=bus,
        )
        services = EnterpriseServices(
            lifecycle_manager=lifecycle,
            resource_manager=resources,
            health_monitor=health,
            telemetry=telemetry,
        )

        received = []
        bus.subscribe(
            "scheduler.task_queued",
            lambda payload: received.append(payload),
        )

        resources.register("workers", capacity=2)
        resources.acquire("workers")
        lifecycle.register_service("api")

        scheduler = EnterpriseScheduler(event_bus=bus)
        scheduler.register_handler(
            "start_service",
            lambda payload: lifecycle.start_service(payload["name"]),
        )
        scheduler.submit_task(
            "integration-start-api",
            "start_service",
            payload={"name": "api"},
        )
        scheduler.execute_next()

        self.assertEqual(lifecycle.get_service("api")["state"], "RUNNING")
        self.assertTrue(received)
        self.assertTrue(bus.history())
        self.assertIsNotNone(supervisor.inspect())

        health.register_check("api", lambda: True)
        health.run_checks()
        self.assertIsNotNone(health.report())

        telemetry.increment("eos.integration.success")
        self.assertTrue(telemetry.snapshot())

        services.register("lifecycle_manager", lifecycle)
        self.assertIs(services.require("lifecycle_manager"), lifecycle)
        self.assertTrue(services.diagnostics()["integrations"]["telemetry"])

        lifecycle.stop_service("api")
        resources.release("workers")
        self.assertEqual(lifecycle.get_service("api")["state"], "STOPPED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
