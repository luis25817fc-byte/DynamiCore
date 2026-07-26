from abc import ABC, abstractmethod

from app.core.intelligence.enterprise_models import (
    Decision,
    Prediction,
    Evidence,
    TwinState,
    SimulationResult
)


class PredictionProvider(ABC):

    @abstractmethod
    def predict(self, twin: TwinState) -> Prediction:
        raise NotImplementedError


class DecisionProvider(ABC):

    @abstractmethod
    def decide(
        self,
        prediction: Prediction
    ) -> Decision:
        raise NotImplementedError


class EvidenceProvider(ABC):

    @abstractmethod
    def collect(self) -> Evidence:
        raise NotImplementedError


class TwinProvider(ABC):

    @abstractmethod
    def current_state(self) -> TwinState:
        raise NotImplementedError


class SimulationProvider(ABC):

    @abstractmethod
    def simulate(
        self,
        twin: TwinState
    ) -> SimulationResult:
        raise NotImplementedError