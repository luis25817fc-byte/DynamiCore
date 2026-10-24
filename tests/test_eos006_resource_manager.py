import unittest
from app.core.enterprise_os.resource_manager import EnterpriseResourceManager


class TestEnterpriseResourceManager(unittest.TestCase):
    def setUp(self):
        self.rm = EnterpriseResourceManager()

    def test_register_and_acquire(self):
        self.rm.register("cpu", capacity=2)
        self.assertTrue(self.rm.acquire("cpu"))
        self.assertEqual(self.rm.get("cpu")["used"], 1)

    def test_capacity_limit(self):
        self.rm.register("memory", capacity=1)
        self.assertTrue(self.rm.acquire("memory"))
        self.assertFalse(self.rm.acquire("memory"))

    def test_release(self):
        self.rm.register("worker", capacity=2)
        self.rm.acquire("worker")
        self.rm.release("worker")
        self.assertEqual(self.rm.get("worker")["status"], "AVAILABLE")

    def test_invalid_release(self):
        self.rm.register("disk", capacity=2)
        with self.assertRaises(ValueError):
            self.rm.release("disk")

    def test_cannot_remove_in_use(self):
        self.rm.register("process", capacity=1)
        self.rm.acquire("process")
        with self.assertRaises(RuntimeError):
            self.rm.remove("process")

    def test_unknown_resource(self):
        with self.assertRaises(KeyError):
            self.rm.get("missing")


if __name__ == "__main__":
    unittest.main()
