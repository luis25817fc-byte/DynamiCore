import jwt
import datetime

SECRET = "super-secret-dynamicore"


def create_token(api_key: str):
    payload = {
        "api_key": api_key,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        return None
