
from .store import SnapshotStore


class SnapshotEngine:


    def __init__(self):

        self.snapshots = []
        self.store = SnapshotStore()


    def save(self, analysis):

        snapshot = {
            "id": len(self.snapshots),
            "analysis": analysis
        }

        self.snapshots.append(snapshot)

        self.store.save(snapshot)

        return snapshot



    def all(self):

        return self.store.load()



    def latest(self):

        if self.snapshots:
            return self.snapshots[-1]

        return self.store.latest()
