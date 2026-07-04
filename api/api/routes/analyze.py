from fastapi import APIRouter
from api.core.analyzer import DynamiCore

router = APIRouter()
engine = DynamiCore()

@router.post("/analyze-system")
def analyze(payload: dict):

    system = payload.get("system", [])

    if not system:
        return {"error": "system required"}

    result = engine.analyze(system)

    return {
        "success": True,
        "payload": result
    }
