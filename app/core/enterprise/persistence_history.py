
from datetime import datetime


class EnterprisePersistenceHistory:

    VERSION = "6.6.5"

    def __init__(self):
        self.history = []


    def save(
        self,
        state
    ):

        record = {
            "timestamp": str(datetime.utcnow()),
            "state": state
        }

        self.history.append(
            record
        )

        return {
            "version": self.VERSION,
            "saved": True,
            "records": len(self.history)
        }


    def get_history(self):

        return {
            "version": self.VERSION,
            "records": len(self.history),
            "history": self.history
        }
