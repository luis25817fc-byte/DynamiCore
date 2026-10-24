import json
import tempfile
import unittest
from pathlib import Path

from app.core.enterprise_os.scheduler import EnterpriseScheduler


class TestEnterpriseScheduler(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.state = Path(self.tmp.name) / "scheduler.json"
        self.scheduler = EnterpriseScheduler(storage_path=self.state)

    def tearDown(self):
        self.tmp.cleanup()

    def test_legacy_api_and_empty_queue(self):
        self.assertEqual(self.scheduler.next_task(), {"status": "EMPTY"})
        task = self.scheduler.submit_task("t1", "noop")
        self.assertEqual(task["status"], "QUEUED")
        self.assertEqual(self.scheduler.queue_status()[0]["task_id"], "t1")
        self.assertEqual(self.scheduler.diagnostics()["queued_tasks"], 1)

    def test_priority_order(self):
        self.scheduler.submit_task("low", "noop", priority="LOW")
        self.scheduler.submit_task("normal", "noop", priority="NORMAL")
        self.scheduler.submit_task("critical", "noop", priority="CRITICAL")
        self.assertEqual(self.scheduler.next_task()["task_id"], "critical")
        self.assertEqual(self.scheduler.next_task()["task_id"], "normal")
        self.assertEqual(self.scheduler.next_task()["task_id"], "low")

    def test_future_tasks_wait(self):
        self.scheduler.submit_task("later", "noop", run_at=9999999999)
        self.assertEqual(self.scheduler.next_task()["status"], "EMPTY")
        self.assertEqual(len(self.scheduler.queue_status()), 1)

    def test_idempotency_and_duplicate_ids(self):
        a = self.scheduler.submit_task(
            "one", "noop", idempotency_key="request-1"
        )
        b = self.scheduler.submit_task(
            "ignored-new-id", "noop", idempotency_key="request-1"
        )
        self.assertEqual(a["schedule_id"], b["schedule_id"])
        with self.assertRaises(ValueError):
            self.scheduler.submit_task("one", "noop")

    def test_cancel_only_queued_tasks(self):
        self.scheduler.submit_task("cancel-me", "noop")
        self.assertTrue(self.scheduler.cancel("cancel-me"))
        self.assertFalse(self.scheduler.cancel("cancel-me"))
        self.assertEqual(self.scheduler.history()[0]["status"], "CANCELLED")

    def test_registered_handler_executes(self):
        self.scheduler.register_handler("echo", lambda payload: {"got": payload})
        self.scheduler.submit_task("exec", "echo", payload={"x": 7})
        result = self.scheduler.execute_next()
        self.assertEqual(result["status"], "COMPLETED")
        self.assertEqual(result["result"], {"got": {"x": 7}})

    def test_failure_and_retry(self):
        calls = {"n": 0}
        def flaky(payload):
            calls["n"] += 1
            if calls["n"] == 1:
                raise RuntimeError("temporary")
            return "ok"
        self.scheduler.register_handler("flaky", flaky)
        self.scheduler.submit_task(
            "retry", "flaky", max_attempts=2
        )
        first = self.scheduler.execute_next()
        self.assertEqual(first["status"], "QUEUED")
        second = self.scheduler.execute_next()
        self.assertEqual(second["status"], "COMPLETED")
        self.assertEqual(second["attempts"], 2)

    def test_final_failure_is_recorded(self):
        self.scheduler.register_handler(
            "broken", lambda payload: (_ for _ in ()).throw(ValueError("bad"))
        )
        self.scheduler.submit_task("broken-task", "broken")
        result = self.scheduler.execute_next()
        self.assertEqual(result["status"], "FAILED")
        self.assertIn("ValueError", result["last_error"])

    def test_persistence_round_trip(self):
        self.scheduler.submit_task("persist", "noop", payload={"v": 2})
        restored = EnterpriseScheduler(storage_path=self.state)
        self.assertEqual(restored.queue_status()[0]["task_id"], "persist")
        self.assertEqual(restored.queue_status()[0]["payload"], {"v": 2})

    def test_json_payload_validation(self):
        with self.assertRaises(TypeError):
            self.scheduler.submit_task("bad", "noop", payload=object())

    def test_event_bus_integration(self):
        class Bus:
            def __init__(self):
                self.events = []
            def publish(self, event_type, payload):
                self.events.append((event_type, payload))
        bus = Bus()
        scheduler = EnterpriseScheduler(event_bus=bus)
        scheduler.submit_task("evt", "noop")
        scheduler.next_task()
        self.assertEqual(
            [e[0] for e in bus.events],
            ["scheduler.task_queued", "scheduler.task_scheduled"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
