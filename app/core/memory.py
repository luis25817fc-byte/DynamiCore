from app.core.db import SessionLocal
from app.core.models import Message


def save_message(api_key: str, role: str, content: str):
    db = SessionLocal()
    msg = Message(api_key=api_key, role=role, content=content)
    db.add(msg)
    db.commit()
    db.close()


def get_history(api_key: str, limit: int = 10):
    db = SessionLocal()
    messages = (
        db.query(Message)
        .filter(Message.api_key == api_key)
        .order_by(Message.id.desc())
        .limit(limit)
        .all()
    )
    db.close()

    return list(reversed([
        {"role": m.role, "content": m.content}
        for m in messages
    ]))
