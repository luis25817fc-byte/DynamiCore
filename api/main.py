from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.analyze import router as analyze_router

app = FastAPI()

# CORS (IMPORTANTE para frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REGISTRO DE RUTAS
app.include_router(analyze_router)

@app.get("/")
def root():
    return {"status": "DynamiCore API running"}
