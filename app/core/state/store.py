
import json
from pathlib import Path


class SnapshotStore:


    def __init__(self, path="snapshots.json"):

        self.path = Path(path)

        if not self.path.exists():
            self.path.write_text(
                "[]",
                encoding="utf-8"
            )


    def save(self, snapshot):

        data = self.load()

        data.append(snapshot)

        self.path.write_text(
            json.dumps(
                data,
                indent=2
            ),
            encoding="utf-8"
        )

        return snapshot



    def load(self):

        return json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )



    def latest(self):

        data = self.load()

        if not data:
            return None

        return data[-1]
