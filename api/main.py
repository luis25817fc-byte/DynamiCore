from fastapi import FastAPI, Depends, Request
from app.core.db import init_db
from app.core.auth import create_api_key, create_user
from app.core.middleware import require_api_key
from app.core.stripe_service import create_checkout

app = FastAPI(title="DynamiCore SaaS Pro")


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def home():
    return {"status": "DynamiCore PRO running"}


# 👤 SIGNUP
@app.get("/signup")
def signup():
    api_key = create_api_key()
    create_user(api_key)
    return {"api_key": api_key}


# 🧠 CORE API (PROTEGIDO)
@app.post("/analyze")
def analyze(user=Depends(require_api_key)):
    user.requests += 1

    return {
        "result": "analysis completed",
        "plan": user.plan,
        "requests_used": user.requests
    }


# 💳 STRIPE
@app.get("/upgrade/{api_key}")
def upgrade(api_key: str):
    return {"checkout_url": create_checkout(api_key)}


# 🔥 WEBHOOK REAL
@app.post("/stripe/webhook")
async def webhook(request: Request):
    payload = await request.body()
    return {"status": "received"}


@app.get("/success")
def success():
    return {"message": "payment success"}


@app.get("/cancel")
def cancel():
    return {"message": "payment cancelled"}
