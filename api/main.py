from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from app.core.analyzer import DynamiCore

app = FastAPI(title="DynamiCore API", version="1.0.0")

# 🔐 API KEY SIMPLE (MVP PRODUCTO)
VALID_API_KEYS = {
    "dev-key-123": "developer"
}

class SystemRequest(BaseModel):
    system: list[int]

def verify_key(x_api_key: str = Header(None)):
    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.get("/")
def root():
    return {"status": "DynamiCore online"}

@app.post("/analyze")
def analyze(req: SystemRequest, x_api_key: str = Header(None)):
    verify_key(x_api_key)

    engine = DynamiCore(req.system)
    result = engine.analyze()

    return {
        "status": "success",
        "payload": result
    }
