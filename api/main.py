from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from app.core.analyzer import DynamiCore
from app.core.auth import get_user_by_key, check_limit, increment_usage


# =========================
# APP
# =========================
app = FastAPI(
    title="DynamiCore API",
    version="1.0.0"
)


# =========================
# REQUEST MODEL
# =========================
class SystemRequest(BaseModel):
    system: list[int]


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def root():
    return {
        "status": "DynamiCore API online",
        "tier": "production"
    }


# =========================
# ANALYZE ENDPOINT
# =========================
@app.post("/analyze")
def analyze(
    req: SystemRequest,
    x_api_key: str = Header(..., alias="x-api-key")
):

    # 🔐 AUTH
    user, data = get_user_by_key(x_api_key)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    if not check_limit(data):
        raise HTTPException(status_code=429, detail="Limit reached")

    # 🧠 ENGINE
    engine = DynamiCore(req.system)
    result = engine.analyze()

    # 📊 USAGE TRACKING
    increment_usage(user)

    # 🔥 FIX: SERIALIZAR GRAPH PARA FRONTEND
    system = req.system

    graph_json = {
        "nodes": list(range(len(system))),
        "edges": [
            {"from": i, "to": system[i]}
            for i in range(len(system))
        ]
    }

    # 🔁 REEMPLAZAR graph OBJECT SI EXISTE
    if "graph" in result:
        result["graph"] = graph_json

    return {
        "status": "success",
        "user": user,
        "plan": data["plan"],
        "payload": result
    }
