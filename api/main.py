from fastapi import FastAPI
from pydantic import BaseModel

from dynamicore.core.analyzer import DynamiCore

app = FastAPI(
    title="DynamiCore API",
    version="1.0.0",
    description="Deterministic Structural Dynamics Engine"
)

class SystemRequest(BaseModel):
    system: list[int]

@app.get("/")
def root():
    return {
        "status": "online",
        "framework": "DynamiCore"
    }

@app.post("/analyze")
def analyze(req: SystemRequest):

    engine = DynamiCore(req.system)

    return engine.analyze()
