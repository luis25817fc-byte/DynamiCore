from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from openai import OpenAI

app = FastAPI(title="DynamiCore API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI client (usa variable de entorno)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"status": "ok", "message": "DynamiCore API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
async def chat(request: Request):
    try:
        body = await request.json()

        message = body.get("message")
        model = body.get("model", "gpt-4o-mini")  # estable y barato

        if not message:
            raise HTTPException(status_code=400, detail="Message is required")

        # 🔥 llamada a IA real
        response = client.responses.create(
            model=model,
            input=message
        )

        return {
            "response": response.output_text,
            "model": model,
            "status": "success"
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
            }
