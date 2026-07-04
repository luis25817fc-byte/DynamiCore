from sqlalchemy import Column, String, Integer, Text, ForeignKey
from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    api_key = Column(String, primary_key=True, index=True)
    plan = Column(String, default="free")
    requests = Column(Integer, default=0)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    api_key = Column(String, ForeignKey("users.api_key"))
    role = Column(String)  # user / assistant
    content = Column(Text)
