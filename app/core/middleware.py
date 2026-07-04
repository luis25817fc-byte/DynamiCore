# app/core/middleware.py

from fastapi import Header, HTTPException
from app.core.auth import validate_api_key


def get_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key missing")

    if not validate_api_key(x_api_key):
        raise HTTPException(status_code=403, detail="Invalid API key")

    return x_api_key
