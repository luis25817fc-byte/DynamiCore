
"""
DynamiCore V6.10.6
Adaptive Strategy Persistent Intelligence
"""

import json

from pathlib import Path
from datetime import datetime


class AdaptiveStrategyEvolution:

    VERSION = "6.10.6"


    def __init__(
        self,
        storage_path=None
    ):

        if storage_path is None:

            storage_path = (
                Path(__file__).parent /
                "adaptive_strategy_memory.json"
            )

        self.storage_path = Path(
            storage_path
        )

        self.strategies = {}

        self.load()



    def load(self):

        if not self.storage_path.exists():

            self.strategies = {}

            return


        try:

            with open(
                self.storage_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.strategies = json.load(file)

        except Exception:

            self.strategies = {}



    def save(self):

        self.storage_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.storage_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.strategies,
                file,
                indent=4
            )



    def evaluate_strategy(
        self,
        decision,
        feedback
    ):

        action = decision.get(
            "action",
            "UNKNOWN"
        )

        score = feedback.get(
            "score",
            0
        )


        if action not in self.strategies:

            self.strategies[action] = {

                "executions": 0,
                "success": 0,
                "score": 0,
                "history": []

            }


        strategy = self.strategies[action]


        strategy["executions"] += 1


        if score > 0:

            strategy["success"] += 1


        strategy["score"] = (
            strategy["success"]
            /
            strategy["executions"]
        )


        strategy["history"].append({

            "timestamp":
                datetime.utcnow().isoformat(),

            "score":
                score,

            "decision":
                decision

        })


        self.save()


        return {

            "version":
                self.VERSION,

            "strategy":
                action,

            "performance":
                strategy["score"],

            "executions":
                strategy["executions"],

            "success_rate":
                strategy["score"]

        }



    def recommend(self):

        if not self.strategies:

            return {

                "version":
                    self.VERSION,

                "recommended_strategy":
                    "UNKNOWN",

                "confidence":
                    0

            }


        best = max(
            self.strategies,
            key=lambda x:
            self.strategies[x]["score"]
        )


        return {

            "version":
                self.VERSION,

            "recommended_strategy":
                best,

            "confidence":
                self.strategies[best]["score"]

        }



    def status(self):

        return {

            "version":
                self.VERSION,

            "status":
                "ADAPTIVE_STRATEGY_PERSISTENT_ACTIVE",

            "strategies":
                len(self.strategies)

        }
