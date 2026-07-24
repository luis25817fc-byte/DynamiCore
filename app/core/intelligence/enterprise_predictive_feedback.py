from datetime import datetime, timezone



class EnterprisePredictiveFeedback:
    """
    DLIS-060.1

    Predictive Feedback Integration

    Evalúa predicciones contra resultados
    observados y genera aprendizaje.
    """

    VERSION = "1.0"



    def __init__(self):

        self.evaluations = 0

        self.history = []



    def evaluate(
        self,
        prediction,
        actual_state
    ):


        predicted_state = prediction.get(
            "predicted_state"
        )


        correct = (
            predicted_state == actual_state
        )


        error = 0.0 if correct else 1.0



        feedback = {

            "evaluation_id":
                self.evaluations + 1,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "prediction_id":
                prediction.get(
                    "prediction_id"
                ),

            "predicted_state":
                predicted_state,

            "actual_state":
                actual_state,

            "correct":
                correct,

            "prediction_error":
                error,

            "learning_signal":
                (
                    "POSITIVE"
                    if correct
                    else
                    "ADJUST"
                ),

            "version":
                self.VERSION

        }


        self.evaluations += 1


        self.history.append(
            feedback
        )


        return feedback



    def diagnostics(self):

        return {

            "version":
                self.VERSION,

            "evaluations":
                self.evaluations,

            "history_size":
                len(self.history)

        }