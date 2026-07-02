from app.core.db import get_user

def validate_user(api_key):

    user = get_user(api_key)

    if not user:
        return None

    plan = user[2]
    requests = user[3]

    limit = 200 if plan == "free" else 100000

    if requests >= limit:
        return "LIMIT"

    return user
