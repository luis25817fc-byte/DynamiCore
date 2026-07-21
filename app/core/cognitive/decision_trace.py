from datetime import datetime, timezone
import uuid


class DecisionTrace:
    """
    DynamiCore Decision Trace
    V8.0

    Registra el razonamiento y la decisión generada.
    """

    VERSION = "V8.0"


    def __init__(self):

        self.traces = []


    def create(
        self,
        cognitive_output
    ):

        trace = {

            "trace_id":
                str(uuid.uuid4()),

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION,

            "objective":
                cognitive_output
                .get("objective", {}),

            "action":
                cognitive_output
                .get("action", {}),

            "confidence":
                cognitive_output
                .get("confidence", {}),

            "reasoning":
                cognitive_output
                .get("reasoning", {})

        }


        self.traces.append(
            trace
        )


        return trace


    def history(self):

        return {

            "total":
                len(self.traces),

            "traces":
                self.traces

        }
