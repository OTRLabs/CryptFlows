from __future__ import annotations
from pathlib import Path
from rich import get_console
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, Session, sessionmaker
from ....configs.config import Config
from rich.console import Console

from .models.models import *


from sqlalchemy.engine import Engine
class DatabaseUtils:

    def __init__(self, console: Console) -> None:
        console.print("Initializing database...", style="bold green")

        
    def connect_to_database() -> Engine:
        """
        This function connects to the database and returns the database engine.

        Returns:
            Engine: The SQLAlchemy database engine.
        """
        duck_db_engine: Engine = create_engine(
            f"sqlite:///{Config.SQLITE_DB_PATH}",
        )
        return duck_db_engine

        
    def