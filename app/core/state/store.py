
import json
from pathlib import Path


class SnapshotStore:


    def __init__(self, path="snapshots.json"):

        self.path = Path(path)



    def _sanitize(self, obj, seen=None):

        if seen is None:

            seen = set()


        if isinstance(obj, (dict, list)):

            obj_id = id(obj)


            if obj_id in seen:

                return "<circular_reference_removed>"


            seen.add(obj_id)



        if isinstance(obj, dict):

            return {

                str(k):

                self._sanitize(
                    v,
                    seen
                )

                for k, v in obj.items()

            }



        if isinstance(obj, list):

            return [

                self._sanitize(
                    item,
                    seen
                )

                for item in obj

            ]



        if isinstance(obj, (str, int, float, bool)) or obj is None:

            return obj



        return str(obj)



    def save(self, snapshot):


        data = self._sanitize(snapshot)


        self.path.write_text(

            json.dumps(

                data,

                indent=2

            )

        )


        return data



    def load(self):


        if not self.path.exists():

            return []


        try:

            return json.loads(

                self.path.read_text()

            )

        except Exception:

            return []
