from pathlib import Path

from datetime import datetime, timezone
import json


class TraceStore:
    """
    DynamiCore Trace Store
    V8.0

    Persistencia de decisiones cognitivas.
    """

    VERSION = "V8.0"


    def __init__(
        self,
        path="reports/cognitive_traces.json"
    ):

        self.path = Path(
            path
        )

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(
        self,
        trace
    ):

        history = []


        if self.path.exists():

            try:

                history = json.loads(
                    self.path.read_text(
                        encoding="utf-8"
                    )
                )

            except Exception:

                history = []


        history.append(
            trace
        )


        self.path.write_text(
            json.dumps(
                history,
                indent=4
            ),
            encoding="utf-8"
        )


        return {

            "version":
                self.VERSION,

            "saved":
                True,

            "records":
                len(history),

            "path":
                str(self.path)

        }


    def load(self):

        if not self.path.exists():

            return []


        return json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )
