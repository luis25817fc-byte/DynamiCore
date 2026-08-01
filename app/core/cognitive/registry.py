from .cognitive_factory import CognitiveFactory


class CognitiveRegistry(CognitiveFactory):
    """
    Compatibility wrapper.
    DLIS-080 Cognitive Factory migration.
    """

    VERSION = "V8.0"


cognitive_registry = CognitiveRegistry()
