"""
DynamiCore Enterprise Database Layer
SQLAlchemy 2.x
PostgreSQL Ready
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./dynamicore.db"
)


class Base(DeclarativeBase):
    pass


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=40,
    pool_recycle=3600,
    future=True,
    echo=False,
)

SessionLocal = scoped_session(
    sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine,
        expire_on_commit=False,
    )
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def create_database():

    Base.metadata.create_all(bind=engine)
