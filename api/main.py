from fastapi import FastAPI
from api.routes.analyze import router as analyze_router

app = FastAPI(title="DynamiCore API")

app.include_router(analyze_router)
