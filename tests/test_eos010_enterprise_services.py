import unittest
from app.core.enterprise_os.enterprise_services import EnterpriseServices

class TestEnterpriseServices(unittest.TestCase):
    def setUp(self): self.s = EnterpriseServices()

    def test_register_resolve(self):
        obj = object()
        self.s.register("api", obj)
        self.assertIs(self.s.require("api"), obj)

    def test_duplicate_rejected(self):
        self.s.register("api", object())
        with self.assertRaises(ValueError): self.s.register("api", object())

    def test_unknown_rejected(self):
        with self.assertRaises(KeyError): self.s.require("missing")

    def test_unregister(self):
        obj = object()
        self.s.register("api", obj)
        self.assertIs(self.s.unregister("api"), obj)
        self.assertEqual(self.s.list_services(), [])

    def test_metadata_defensive(self):
        meta = {"tags": ["core"]}
        self.s.register("api", object(), meta)
        meta["tags"].append("bad")
        self.assertEqual(self.s.get("api")["metadata"]["tags"], ["core"])

    def test_list_and_diagnostics(self):
        self.s.register("b", object())
        self.s.register("a", object())
        self.assertEqual([x["name"] for x in self.s.list_services()], ["a", "b"])
        self.assertEqual(self.s.diagnostics()["registered_services"], 2)

    def test_integrations_reported(self):
        obj = object()
        s = EnterpriseServices(telemetry=obj)
        self.assertTrue(s.diagnostics()["integrations"]["telemetry"])
        self.assertFalse(s.diagnostics()["integrations"]["health_monitor"])

if __name__ == "__main__": unittest.main()
