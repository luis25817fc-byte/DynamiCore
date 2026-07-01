from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from dynamicore.core.analyzer import DynamiCore
from app.core.auth import get_user_by_key, check_limit, increment_usage

app = FastAPI(
    title="DynamiCore API",
    version="1.0.0"
)

class SystemRequest(BaseModel):
    system: list[int]


@app.get("/")
def root():
    return {
        "status": "DynamiCore API online",
        "tier": "production"
    }


@app.post("/analyze")
def analyze(req: SystemRequest, x_api_key: str = Header(None)):

    # 🔐 AUTH
    user, data = get_user_by_key(x_api_key)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    if not check_limit(data):
        raise HTTPException(status_code=429, detail="Limit reached")

    # 🧠 ENGINE
    engine = DynamiCore(req.system)
    result = engine.analyze()

    # 📊 TRACK USAGE
    increment_usage(user)

    return {
        "status": "success",
        "user": user,
        "plan": data["plan"],
        "payload": result
    }
