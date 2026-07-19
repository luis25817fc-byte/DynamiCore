
from app.core.kernel import StateVector


class StateTransitionEngine:


    def predict(self, state: StateVector, delta):

        return StateVector(

            entropy=(
                state.entropy +
                delta.get("entropy", 0)
            ),

            coherence=(
                state.coherence +
                delta.get("coherence", 0)
            ),

            dynamics=(
                state.dynamics +
                delta.get("dynamics", 0)
            ),

            potential=(
                state.potential +
                delta.get("potential", 0)
            ),

            divergence=(
                state.divergence +
                delta.get("divergence", 0)
            )
        )
