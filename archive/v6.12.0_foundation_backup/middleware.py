from fastapi import Header, HTTPException
from app.core.auth import get_user


def require_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(401, "Missing API key")

    user = get_user(x_api_key)

    if not user:
        raise HTTPException(403, "Invalid API key")

    return user
