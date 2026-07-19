import uuid
from app.core.db import SessionLocal
from app.core.models import User


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
