import unittest

from app.core.enterprise_os.process_manager import ProcessManager
from app.core.enterprise_os.runtime_supervisor import RuntimeSupervisor
from app.core.enterprise_os.event_bus import EventBus


class TestEOS002ProcessManager(unittest.TestCase):
    def test_register_and_list(self):
        pm = ProcessManager()
        pm.register("eos_test_process")
        self.assertIn("eos_test_process", str(pm.list()))

    def test_health_is_callable(self):
        pm = ProcessManager()
        self.assertIsNotNone(pm.health())


class TestEOS003RuntimeSupervisor(unittest.TestCase):
    def test_inspect_process_manager(self):
        pm = ProcessManager()
        supervisor = RuntimeSupervisor(pm)
        result = supervisor.inspect()
        self.assertIsNotNone(result)


class TestEOS004EventBus(unittest.TestCase):
    def test_subscribe_and_publish(self):
        bus = EventBus()
        received = []
        bus.subscribe("EOS_TEST", lambda payload: received.append(payload))
        bus.publish("EOS_TEST", {"value": 42})
        self.assertTrue(received, "El suscriptor no recibió el evento")

    def test_history_and_health(self):
        bus = EventBus()
        bus.publish("EOS_HISTORY_TEST", {"value": 1})
        self.assertIsNotNone(bus.history())
        self.assertIsNotNone(bus.health())


if __name__ == "__main__":
    unittest.main(verbosity=2)
