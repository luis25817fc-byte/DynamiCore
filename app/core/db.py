# app/core/db.py

USERS = {}

def create_user(api_key: str):
    USERS[api_key] = {
        "plan": "free",
        "requests": 0
    }
    return USERS[api_key]


def get_user(api_key: str):
    return USERS.get(api_key)


def upgrade_user(api_key: str):
    if api_key in USERS:
        USERS[api_key]["plan"] = "pro"
