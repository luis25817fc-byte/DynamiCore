import uuid
import jwt
import os
from datetime import datetime, timedelta
from app.core.db import SessionLocal, User

SECRET = os.getenv("JWT_SECRET", "dev-secret")


def create_api_key():
    return str(uuid.uuid4())


def create_user(api_key: str):
    db = SessionLocal()
    user = User(api_key=api_key)
    db.add(user)
    db.commit()
    db.close()
    return api_key


def get_user(api_key: str):
    db = SessionLocal()
    user = db.query(User).filter(User.api_key == api_key).first()
    db.close()
    return user


def encode_jwt(api_key: str):
    payload = {
        "api_key": api_key,
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")


def decode_jwt(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        return None
