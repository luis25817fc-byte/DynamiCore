from fastapi import FastAPI, Depends, Body
from app.core.db import Base, engine
from app.core.auth import create_api_key, create_user, get_user
from app.core.security import require_api_key
from app.core.memory import save_message, get_history
from app.core.ai import run_ai
from app.core.stripe_service import create_checkout

app = FastAPI(title="DynamiCore AI Engine v2")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# HOME
@app.get("/")
def home():
    return {"status": "DynamiCore AI Engine v2 LIVE"}


# SIGNUP
@app.get("/signup")
def signup():
    api_key = create_api_key()
    create_user(api_key)
    return {"api_key": api_key}


# CHAT (CON MEMORIA REAL)
@app.post("/chat")
def chat(
    prompt: str = Body(...),
    user=Depends(require_api_key)
):

    user.requests += 1

    # 🧠 guardar mensaje usuario
    save_message(user.api_key, "user", prompt)

    # 📚 historial
    history = get_history(user.api_key)

    # 🧠 IA
    response = run_ai(history)

    # 💾 guardar respuesta
    save_message(user.api_key, "assistant", response)

    return {
        "response": response,
        "usage": user.requests
    }


# ANALYZE
@app.post("/analyze")
def analyze(user=Depends(require_api_key)):
    user.requests += 1
    return {"status": "ok", "requests": user.requests}


# STRIPE
@app.get("/upgrade/{api_key}")
def upgrade(api_key: str):
    return {"checkout_url": create_checkout(api_key)}
