from fastapi import FastAPI
from pydantic import BaseModel

from dynamicore.core.analyzer import DynamiCore

app = FastAPI(
    title="DynamiCore API",
    version="1.0.0",
    description="Commercial API for DynamiCore"
)

class AnalyzeRequest(BaseModel):
    system: list[int]

@app.get("/")
def root():
    return {
        "framework": "DynamiCore",
        "status": "online",
        "version": "1.0.0"
    }

@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    engine = DynamiCore(request.system)

    result = engine.analyze()

    return result
