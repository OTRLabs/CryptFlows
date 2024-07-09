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

from .models.models import *


from sqlalchemy.engine import Engine

def connect_to_database() -> Engine:
    """
    This function connects to the database and returns the database engine.

    Returns:
        Engine: The SQLAlchemy database engine.
    """
    duck_db_engine: Engine = create_engine(
        f"duckdb:///{Config.DUCKDB_PATH}",
    )
    return duck_db_engine

    