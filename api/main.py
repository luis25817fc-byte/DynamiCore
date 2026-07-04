from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.analyze import router as analyze_router
from api.routes.explain import router as explain_router

app = FastAPI(title="DynamiCore Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(analyze_router)
app.include_router(explain_router)

@app.get("/")
def root():
    return {
        "status": "DynamiCore Engine online",
        "version": "1.0.0"
    }
