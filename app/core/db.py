import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    api_key = Column(String, primary_key=True, index=True)
    plan = Column(String, default="free")
    requests = Column(Integer, default=0)


def init_db():
    Base.metadata.create_all(bind=engine)
