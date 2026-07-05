# api/routes/analyze.py

from fastapi import APIRouter, Request
from api.core.engine import DynamiCoreEngine

router = APIRouter()
engine = DynamiCoreEngine()

@router.post("/analyze")
async def analyze(request: Request):

    data = await request.json()
    system = data.get("system", [])

    return {
        "status": "success",
        "results": engine.analyze(system)
    }
