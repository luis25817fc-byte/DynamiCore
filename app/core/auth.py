from app.core.db import get_user

def validate_key(api_key: str):
    user = get_user(api_key)

    if not user:
        return None

    requests = user[2]
    limit = user[3]

    if requests >= limit:
        return "LIMIT"

    return user
