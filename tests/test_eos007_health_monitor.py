import unittest
from app.core.enterprise_os.health_monitor import EnterpriseHealthMonitor


class TestEnterpriseHealthMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = EnterpriseHealthMonitor()

    def test_healthy_check(self):
        self.monitor.register_check("api", lambda: True)
        report = self.monitor.run_checks()
        self.assertEqual(report["status"], "HEALTHY")
        self.assertEqual(report["checks_passed"], 1)

    def test_critical_failure(self):
        self.monitor.register_check("database", lambda: False)
        self.assertEqual(self.monitor.run_checks()["status"], "UNHEALTHY")

    def test_optional_failure_degrades(self):
        self.monitor.register_check("cache", lambda: False, critical=False)
        self.assertEqual(self.monitor.run_checks()["status"], "DEGRADED")

    def test_exception_is_reported(self):
        def broken():
            raise RuntimeError("probe failed")
        self.monitor.register_check("probe", broken)
        report = self.monitor.run_checks()
        self.assertEqual(report["checks"]["probe"]["status"], "ERROR")
        self.assertEqual(report["status"], "UNHEALTHY")

    def test_duplicate_and_invalid_check(self):
        self.monitor.register_check("api", lambda: True)
        with self.assertRaises(ValueError):
            self.monitor.register_check("api", lambda: True)
        with self.assertRaises(TypeError):
            self.monitor.register_check("bad", "not callable")

    def test_unregister_and_report_copy(self):
        self.monitor.register_check("api", lambda: True)
        report = self.monitor.run_checks()
        report["checks"]["api"]["status"] = "CORRUPTED"
        self.assertEqual(self.monitor.report()["checks"]["api"]["status"], "HEALTHY")
        self.assertTrue(self.monitor.unregister_check("api"))
        self.assertFalse(self.monitor.unregister_check("api"))
        self.assertEqual(self.monitor.run_checks()["checks_total"], 0)


if __name__ == "__main__":
    unittest.main()
