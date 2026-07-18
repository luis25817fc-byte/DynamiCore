
from pathlib import Path
import json


class RuntimePersistenceV741:


    VERSION = "7.4.1"


    def __init__(self, storage_path=None):

        self.storage_path = Path(
            storage_path or
            "/content/drive/MyDrive/DynamiCore/runtime_storage"
        )

        self.storage_path.mkdir(
            parents=True,
            exist_ok=True
        )

        self.events_file = self.storage_path / "events.json"
        self.states_file = self.storage_path / "states.json"
        self.transitions_file = self.storage_path / "transitions.json"

        self.initialize_storage()



    def initialize_storage(self):

        for file in [
            self.events_file,
            self.states_file,
            self.transitions_file
        ]:

            if not file.exists():

                file.write_text(
                    "[]",
                    encoding="utf-8"
                )



    def load_data(self, file):

        return json.loads(
            file.read_text(
                encoding="utf-8"
            )
        )



    def save_data(self, file, data):

        file.write_text(
            json.dumps(
                data,
                indent=4,
                default=str
            ),
            encoding="utf-8"
        )



    def save_event(self, event):

        data = self.load_data(
            self.events_file
        )

        data.append(event)

        self.save_data(
            self.events_file,
            data
        )

        return True



    def save_state(self, state):

        data = self.load_data(
            self.states_file
        )

        data.append(state)

        self.save_data(
            self.states_file,
            data
        )

        return True



    def save_transition(self, transition):

        data = self.load_data(
            self.transitions_file
        )

        data.append(transition)

        self.save_data(
            self.transitions_file,
            data
        )

        return True



    def status(self):

        return {

            "version":
                self.VERSION,

            "module":
                "RuntimePersistenceV741",

            "status":
                "ONLINE"

        }
