from __future__ import annotations
from pathlib import Path
from rich import get_console
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, Session, sessionmaker
from ....configs.config import Config
from advanced_alchemy.base import UUIDBase
from advanced_alchemy.filters import LimitOffset
from advanced_alchemy.repository import SQLAlchemySyncRepository
from advanced_alchemy.utils.fixtures import open_fixture
def create_database():
    
    duck_db_engine = create_engine(
        f"duckdb:///{Config.DUCK_DB_PATH}",
        connect_args={"check_same_thread": False},
    )
    
    