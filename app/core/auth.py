# app/core/auth.py

import uuid
from app.core.db import create_user, get_user


def generate_api_key():
    api_key = str(uuid.uuid4())
    create_user(api_key)
    return api_key


def validate_api_key(api_key: str):
    user = get_user(api_key)
    return user is not None
