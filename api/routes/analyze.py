
from fastapi import APIRouter
from pydantic import BaseModel

from app.core.engine import DynamiCoreEngine

router = APIRouter()


class AnalyzeRequest(BaseModel):
    system: list[float]
    metadata: dict | None = None


@router.post("/analyze")
def analyze(req: AnalyzeRequest):

    engine = DynamiCoreEngine()

    result = engine.analyze(req.system)

    return {
        "status": "ok",
        "engine": "DynamiCore Enterprise",
        "metadata": req.metadata,
        "analysis": result
    }
