from typing import Tuple, Optional

# =========================
# BASE DE USUARIOS (MVP SaaS)
# =========================
USERS = {
    "dev": {
        "api_key": "dev-key-123",
        "plan": "free",
        "requests": 0,
        "limit": 1000
    }
}


# =========================
# OBTENER USUARIO POR API KEY
# =========================
def get_user_by_key(api_key: str) -> Tuple[Optional[str], Optional[dict]]:
    for user, data in USERS.items():
        if data["api_key"] == api_key:
            return user, data
    return None, None


# =========================
# VALIDAR LIMITE DE USO
# =========================
def check_limit(user_data: dict) -> bool:
    return user_data["requests"] < user_data["limit"]


# =========================
# INCREMENTAR USO
# =========================
def increment_usage(user: str):
    if user in USERS:
        USERS[user]["requests"] += 1


# =========================
# CREAR USUARIO (FUTURO SAAS)
# =========================
def create_user(username: str, api_key: str, plan: str = "free"):
    USERS[username] = {
        "api_key": api_key,
        "plan": plan,
        "requests": 0,
        "limit": 1000 if plan == "free" else 10000
  }
