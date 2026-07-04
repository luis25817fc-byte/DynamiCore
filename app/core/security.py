import jwt
import datetime
from jwt import ExpiredSignatureError, InvalidTokenError
import os

SECRET = os.getenv("JWT_SECRET", "dev-secret")


def create_token(api_key: str):
    payload = {
        "api_key": api_key,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    if isinstance(token, bytes):
        token = token.decode("utf-8")

    return token


def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])

    except ExpiredSignatureError:
        return {"error": "token_expired"}

    except InvalidTokenError:
        return {"error": "invalid_token"}

    except Exception:
        return {"error": "unknown_error"}
