from datetime import datetime, timezone



class EnterpriseKnowledgeMemory:
    """
    DLIS-059

    Enterprise Knowledge & Memory Layer

    Almacena experiencias cognitivas
    y conocimiento operacional.
    """

    VERSION = "1.0"



    def __init__(self):

        self.entries = []

        self.memory_id = 0



    def store(
        self,
        experience
    ):

        self.memory_id += 1


        record = {

            "memory_id":
                self.memory_id,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "experience":
                experience,

            "version":
                self.VERSION

        }


        self.entries.append(
            record
        )


        return record



    def retrieve_all(self):

        return self.entries



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "memory_entries":
                len(self.entries),

            "latest_id":
                self.memory_id

        }