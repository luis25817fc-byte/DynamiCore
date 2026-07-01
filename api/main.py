from fastapi import FastAPI
from pydantic import BaseModel
from dynamicore.core.analyzer import DynamiCore

app = FastAPI(
    title="DynamiCore API",
    version="1.0.0"
)

class SystemRequest(BaseModel):
    system: list[int]

@app.get("/")
def root():
    return {"status": "online"}

@app.post("/analyze")
def analyze(req: SystemRequest):
    engine = DynamiCore(req.system)
    return engine.analyze()
