from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.core.analyzer import DynamiCore

app = FastAPI(title="DynamiCore API", version="3.0")

# =========================
# INPUT
# =========================
class SystemRequest(BaseModel):
    system: list[int]


# =========================
# FRONTEND SIMPLE (HTML)
# =========================
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return open("templates/index.html", "r", encoding="utf-8").read()


# =========================
# API CORE
# =========================
@app.post("/analyze")
def analyze(req: SystemRequest, x_api_key: str = Header(..., alias="x-api-key")):

    if x_api_key != "dev-key-123":
        raise HTTPException(status_code=401, detail="Invalid API Key")

    engine = DynamiCore(req.system)
    result = engine.analyze()

    return {
        "status": "success",
        "payload": result
    }
