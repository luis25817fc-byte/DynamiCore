
from .state.evolution import EvolutionEngine
from .adaptation.evolution_service import EvolutionService


# IMPORTANTE:
# Este archivo mantiene la arquitectura actual.
# Solo separa EvolutionEngine y EvolutionService.


# Busca tu clase DynamiCoreEngine original y reemplaza únicamente
# las asignaciones del constructor por:

self.evolution_engine = EvolutionEngine()

self.evolution = EvolutionService()
