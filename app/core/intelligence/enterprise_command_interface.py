from datetime import datetime, timezone
import uuid


class EnterpriseCommandInterface:
    """
    DLIS-067.1

    Enterprise Command Interface Layer

    Entrada principal de objetivos
    empresariales hacia DynamiCore.
    """

    VERSION = "2.0"


    def __init__(self):

        self.sessions = []


    def submit_command(
        self,
        user,
        objective,
        priority="NORMAL"
    ):

        command = {

            "command_id":
                str(uuid.uuid4()),

            "user":
                user,

            "objective":
                objective,

            "priority":
                priority,

            "status":
                "RECEIVED",

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        self.sessions.append(
            command
        )


        return command



    def history(self):

        return self.sessions



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "commands":
                len(
                    self.sessions
                ),

            "status":
                "READY"

        }