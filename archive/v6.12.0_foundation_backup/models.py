from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from api.db import Base

class User(Base):
    __tablename__ = "users"

    api_key = Column(String, primary_key=True, index=True)
    plan = Column(String, default="free")
    requests = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class UsageLog(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    api_key = Column(String)
    endpoint = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
