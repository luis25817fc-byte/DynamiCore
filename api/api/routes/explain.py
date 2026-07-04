from fastapi import APIRouter
from api.core.analyzer import DynamiCore

router = APIRouter()
engine = DynamiCore()

@router.post("/explain-system")
def explain(payload: dict):

    system = payload.get("system", [])
    r = engine.analyze(system)

    entropy = r["entropy"]
    coherence = r["coherence"]

    if entropy > 2:
        state = "Highly chaotic system"
    elif coherence > 0.7:
        state = "Stable structured system"
    else:
        state = "Transitioning system"

    return {
        "success": True,
        "interpretation": state,
        "metrics": r
    }
