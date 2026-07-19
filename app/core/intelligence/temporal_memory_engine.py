
from pathlib import Path
import json
from datetime import datetime


class TemporalMemoryEngineV75:

    VERSION = "7.5.0"

    def __init__(self, storage_path=None):

        self.storage = Path(
            storage_path or
            "/content/drive/MyDrive/DynamiCore/runtime_storage"
        )

        self.events_file = self.storage / "events.json"
        self.states_file = self.storage / "states.json"
        self.transitions_file = self.storage / "transitions.json"

    def _load(self, file):

        if not file.exists():
            return []

        return json.loads(file.read_text(encoding="utf-8"))

    def events(self):
        return self._load(self.events_file)

    def states(self):
        return self._load(self.states_file)

    def transitions(self):
        return self._load(self.transitions_file)

    def latest_state(self):

        data = self.states()

        if not data:
            return None

        return data[-1]

    def evolution_summary(self):

        return {
            "version": self.VERSION,
            "events": len(self.events()),
            "states": len(self.states()),
            "transitions": len(self.transitions()),
            "latest": self.latest_state(),
            "generated": str(datetime.utcnow()),
            "status": "ONLINE"
        }

    def status(self):

        return {
            "version": self.VERSION,
            "module": "TemporalMemoryEngineV75",
            "status": "ONLINE"
        }
