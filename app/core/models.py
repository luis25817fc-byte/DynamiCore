from sqlalchemy import Column, String, Integer
from app.core.db import Base

class User(Base):
    __tablename__ = "users"

    api_key = Column(String, primary_key=True, index=True)
    plan = Column(String, default="free")
    requests = Column(Integer, default=0)
