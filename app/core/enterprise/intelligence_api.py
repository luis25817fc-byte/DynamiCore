
class IntelligenceAPI:

    VERSION = "6.6.2"

    def __init__(
        self,
        runtime,
        stream
    ):
        self.runtime = runtime
        self.stream = stream


    def status(self):

        return {
            "version": self.VERSION,
            "runtime": self.runtime.heartbeat(),
            "stream": self.stream.snapshot()
        }


    def ingest(self, event):

        return self.stream.push(event)


    def health(self):

        return {
            "version": self.VERSION,
            "status": "HEALTHY"
        }
