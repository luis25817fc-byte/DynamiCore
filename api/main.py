from fastapi import FastAPI
from pydantic import BaseModel
from dynamicore.core.analyzer import DynamiCore

app = FastAPI(
    title="DynamiCore API",
    version="1.0.0",
    description="DynamiCore Deterministic Structural Dynamics Engine"
)


class SystemRequest(BaseModel):
    system: list[int]


@app.get("/")
def root():
    return {
        "status": "online",
        "framework": "DynamiCore",
        "version": "1.0.0"
    }


@app.post("/analyze")
def analyze(req: SystemRequest):
    engine = DynamiCore(req.system)

    result = engine.analyze()

    # Eliminar objetos que FastAPI no puede convertir a JSON
    if "graph" in result:
        del result["graph"]

    # Convertir las llaves de basins a texto
    if "basins" in result:
        result["basins"] = {
            str(key): value
            for key, value in result["basins"].items()
        }

    return {
        "status": "success",
        "payload": result
    }
