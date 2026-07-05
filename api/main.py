
from fastapi import FastAPI
from api.routes.analyze import router as analyze_router

app = FastAPI(
    title="DynamiCore API",
    version="0.1.0"
)

app.include_router(analyze_router)

@app.get("/")
def root():
    return {
        "status": "online",
        "service": "DynamiCore API",
        "version": "0.1.0"
    }
