import unittest
from app.core.enterprise_os.telemetry import EnterpriseTelemetry

class TestTelemetry(unittest.TestCase):
    def setUp(self): self.t = EnterpriseTelemetry()

    def test_counter(self):
        self.t.increment("requests", 2)
        self.assertEqual(self.t.increment("requests")["value"], 3)

    def test_gauge(self):
        self.assertEqual(self.t.set_gauge("load", 0.7)["value"], 0.7)

    def test_observations(self):
        self.t.observe("latency", 2)
        m = self.t.observe("latency", 4)
        self.assertEqual((m["count"], m["total"], m["min"], m["max"]), (2, 6, 2, 4))

    def test_labels_separate_metrics(self):
        self.t.increment("jobs", labels={"state":"ok"})
        self.t.increment("jobs", labels={"state":"bad"})
        self.assertEqual(self.t.snapshot()["metric_count"], 2)

    def test_snapshot_is_defensive(self):
        self.t.increment("x")
        s = self.t.snapshot()
        s["metrics"][0]["value"] = 999
        self.assertEqual(self.t.snapshot()["metrics"][0]["value"], 1)

    def test_reset(self):
        self.t.increment("a")
        self.t.increment("b")
        self.t.reset("a")
        self.assertEqual(self.t.snapshot()["metric_count"], 1)

    def test_invalid_values_and_type_conflict(self):
        with self.assertRaises(ValueError): self.t.increment("x", -1)
        self.t.increment("x")
        with self.assertRaises(ValueError): self.t.set_gauge("x", 2)

if __name__ == "__main__": unittest.main()
