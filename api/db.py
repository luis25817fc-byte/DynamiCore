
"""
DynamiCore V6.12.0
Enterprise Database Layer
"""

import os

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///dynamicore.db"
)


engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
    if DATABASE_URL.startswith("sqlite")
    else {}
)


Base = declarative_base()


def get_engine():

    return engine
