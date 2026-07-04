from fastapi import FastAPI, Depends
from app.core.auth import generate_api_key
from app.core.middleware import get_api_key
from app.core.db import get_user, upgrade_user
from app.core.stripe_service import create_checkout_session

app = FastAPI(title="DynamiCore SaaS")


# 🏠 HOME
@app.get("/")
def home():
    return {"status": "DynamiCore running"}


# 👤 SIGNUP
@app.get("/signup")
def signup():
    api_key = generate_api_key()
    return {"api_key": api_key}


# 🧠 CORE ANALYSIS (PROTEGIDO)
@app.post("/analyze")
def analyze(api_key: str = Depends(get_api_key)):
    user = get_user(api_key)
    user["requests"] += 1

    return {
        "result": "analysis done",
        "plan": user["plan"],
        "requests_used": user["requests"]
    }


# 💳 STRIPE CHECKOUT
@app.get("/upgrade/{api_key}")
def upgrade(api_key: str):
    url = create_checkout_session(api_key)
    return {"checkout_url": url}


# 🔥 STRIPE WEBHOOK (BÁSICO)
@app.post("/stripe/webhook")
def stripe_webhook():
    # simplificado (luego lo hacemos seguro con signature)
    return {"status": "received"}


# 🎯 SUCCESS
@app.get("/success")
def success():
    return {"message": "Payment successful"}


@app.get("/cancel")
def cancel():
    return {"message": "Payment cancelled"}
