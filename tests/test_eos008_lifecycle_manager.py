import unittest
from app.core.enterprise_os.lifecycle_manager import EnterpriseLifecycleManager


class FakeProcessManager:
    def __init__(self):
        self.registered = []
        self.started = []
        self.stopped = []

    def register(self, name, metadata=None):
        self.registered.append(name)

    def start(self, name):
        self.started.append(name)

    def stop(self, name):
        self.stopped.append(name)


class TestEnterpriseLifecycleManager(unittest.TestCase):
    def setUp(self):
        self.pm = FakeProcessManager()
        self.manager = EnterpriseLifecycleManager(process_manager=self.pm)

    def test_register_and_start(self):
        self.manager.register_service("api", metadata={"tier": 1})
        result = self.manager.start_service("api")
        self.assertEqual(result["state"], "RUNNING")
        self.assertEqual(self.pm.started, ["api"])

    def test_stop_service(self):
        self.manager.register_service("worker")
        self.manager.start_service("worker")
        self.assertEqual(self.manager.stop_service("worker")["state"], "STOPPED")
        self.assertEqual(self.pm.stopped, ["worker"])

    def test_duplicate_and_unknown(self):
        self.manager.register_service("api")
        with self.assertRaises(ValueError):
            self.manager.register_service("api")
        with self.assertRaises(KeyError):
            self.manager.start_service("missing")

    def test_start_failure_is_recorded(self):
        def broken():
            raise RuntimeError("startup failed")
        self.manager.register_service("bad", start_callback=broken)
        with self.assertRaises(RuntimeError):
            self.manager.start_service("bad")
        self.assertEqual(self.manager.get_service("bad")["state"], "FAILED")
        self.assertEqual(self.manager.health()["status"], "UNHEALTHY")

    def test_start_all_and_stop_all_reverse_order(self):
        self.manager.register_service("first")
        self.manager.register_service("second")
        self.assertEqual(len(self.manager.start_all()), 2)
        self.assertEqual(len(self.manager.stop_all()), 2)
        self.assertEqual(self.pm.stopped, ["second", "first"])

    def test_invalid_callback_and_unregister_not_required(self):
        with self.assertRaises(TypeError):
            self.manager.register_service("bad", start_callback="no")
        self.manager.register_service("ok")
        report = self.manager.diagnostics()
        self.assertEqual(report["component"], "EOS-008")
        self.assertEqual(report["health"]["services_total"], 1)

    def test_defensive_copy_and_idempotent_start(self):
        self.manager.register_service("api", metadata={"x": 1})
        view = self.manager.get_service("api")
        view["metadata"]["x"] = 999
        self.assertEqual(self.manager.get_service("api")["metadata"]["x"], 1)
        self.manager.start_service("api")
        self.manager.start_service("api")
        self.assertEqual(self.pm.started, ["api"])


if __name__ == "__main__":
    unittest.main()
