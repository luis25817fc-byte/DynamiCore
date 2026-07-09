
from fastapi import FastAPI

app = FastAPI(
    title="DynamiCore API",
    version="1.0.0"
)

from api.routes.analyze import router as analyze_router

app.include_router(
    analyze_router,
    prefix="/api",
    tags=["DynamiCore"]
)


try:
    from api.routes.explain import router as explain_router

    app.include_router(
        explain_router,
        prefix="/api",
        tags=["Explain"]
    )
except Exception:
    pass


try:
    from api.routes.auth import router as auth_router

    app.include_router(
        auth_router,
        prefix="/api",
        tags=["Auth"]
    )
except Exception:
    pass


@app.get("/")
def root():
    return {
        "status": "online",
        "engine": "DynamiCore Enterprise"
    }
