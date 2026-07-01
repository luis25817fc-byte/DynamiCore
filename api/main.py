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

    try:
        # 🧠 ENGINE
        engine = DynamiCore(req.system)
        result = engine.analyze()

        # 🔥 FORZAR JSON SEGURO (IMPORTANTE)
        payload = {
            "system": list(req.system),
            "cycles": result.get("cycles", []),
            "basins": result.get("basins", {}),
            "entropy": float(result.get("entropy", 0)),
            "coherence": float(result.get("coherence", 0)),

            # 📊 GRAPH YA LIMPIO PARA FRONTEND
            "graph": {
                "nodes": result["graph"]["nodes"],
                "edges": result["graph"]["edges"]
            }
        }

        # 📊 USAGE TRACKING
        increment_usage(user)

        return {
            "status": "success",
            "user": user,
            "plan": data["plan"],
            "payload": payload
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
    }
