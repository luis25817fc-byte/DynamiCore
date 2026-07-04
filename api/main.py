from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="DynamiCore API", version="1.0.0")

# CORS para frontend (Replit / dominio / SaaS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción lo restringimos luego
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check (IMPORTANTE para Render)
@app.get("/")
def home():
    return {"status": "ok", "message": "DynamiCore API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# CHAT ENDPOINT (SaaS CORE)
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()

    message = body.get("message", "")
    model = body.get("model", "gpt-4-turbo")

    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    # 🔥 Aquí luego conectas OpenAI real
    response = f"DynamiCore recibió: {message}"

    return {
        "response": response,
        "model": model,
        "status": "success"
    }
