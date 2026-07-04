from fastapi import FastAPI, Request
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

# CLIENTE OPENAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"status": "ok", "message": "DynamiCore API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# CHAT REAL
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()

    message = body.get("message")

    if not message:
        return {
            "success": False,
            "error": "Message is required"
        }

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=message
        )

        return {
            "success": True,
            "response": response.output_text
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
