from datetime import datetime, timezone
import uuid


class EnterpriseAgentOptimization:
    """
    DLIS-066D.5

    Agent Optimization & Evolution Layer

    Selecciona estrategias basadas
    en rendimiento histórico.
    """

    VERSION = "2.0"


    def __init__(self):

        self.agent_metrics = {}
        self.optimizations = []


    def register_performance(
        self,
        agent,
        score
    ):

        if agent not in self.agent_metrics:

            self.agent_metrics[agent] = []


        self.agent_metrics[agent].append(
            score
        )


        return {

            "agent":
                agent,

            "score":
                score,

            "registered":
                True,

            "version":
                self.VERSION

        }



    def calculate_ranking(self):

        ranking = []


        for agent, scores in self.agent_metrics.items():

            average = sum(scores) / len(scores)

            ranking.append({

                "agent":
                    agent,

                "score":
                    average

            })


        ranking.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return ranking



    def recommend_agent(
        self
    ):

        ranking = self.calculate_ranking()


        if not ranking:

            return None


        recommendation = {

            "optimization_id":
                str(uuid.uuid4()),

            "recommended_agent":
                ranking[0]["agent"],

            "score":
                ranking[0]["score"],

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "version":
                self.VERSION

        }


        self.optimizations.append(
            recommendation
        )


        return recommendation



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "agents":
                len(
                    self.agent_metrics
                ),

            "optimizations":
                len(
                    self.optimizations
                ),

            "status":
                "READY"

        }