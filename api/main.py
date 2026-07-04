from fastapi import FastAPI, Depends, Body
from slowapi.middleware import SlowAPIMiddleware

from app.core.db import Base, engine
from app.core.auth import create_api_key, create_user
from app.core.security import require_api_key
from app.core.stripe_service import create_checkout
from app.core.ai import run_ai

from sqlalchemy.orm import Session

app = FastAPI(title="DynamiCore AI Engine v1")

app.add_middleware(SlowAPIMiddleware)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# HOME
@app.get("/")
def home():
    return {"status": "DynamiCore AI Engine LIVE"}


# SIGNUP
@app.get("/signup")
def signup():
    api_key = create_api_key()
    create_user(api_key)
    return {"api_key": api_key}


# ANALYZE (NO IA)
@app.post("/analyze")
def analyze(user=Depends(require_api_key)):
    user.requests += 1
    return {
        "status": "ok",
        "requests": user.requests
    }


# IA ENGINE (ESTO ES LO IMPORTANTE)
@app.post("/chat")
def chat(
    prompt: str = Body(...),
    user=Depends(require_api_key)
):

    user.requests += 1

    result = run_ai(
        prompt=prompt,
        user_context={
            "api_key": user.api_key,
            "plan": user.plan
        }
    )

    return {
        "input": prompt,
        "output": result["response"],
        "model": result["model"],
        "requests_used": user.requests
    }


# STRIPE UPGRADE
@app.get("/upgrade/{api_key}")
def upgrade(api_key: str):
    return {"checkout_url": create_checkout(api_key)}


@app.get("/success")
def success():
    return {"status": "payment_success"}


@app.get("/cancel")
def cancel():
    return {"status": "payment_cancelled"}
