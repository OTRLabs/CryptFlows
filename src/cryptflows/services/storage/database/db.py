from __future__ import annotations
from pathlib import Path
from rich import get_console
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from sqlalchemy.engine import Engine
from rich.console import Console
from ....configs.config import Config
from .models.models import *

Base = declarative_base()

class DatabaseUtils:
    def __init__(self, console: Console) -> None:
        self.console = console
        self.console.print("Initializing database...", style="bold green")
        self.engine: Engine = self.connect_to_database()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def connect_to_database(self) -> Engine:
        """
        Connect to the SQLite database and return the engine.
        Returns:
            Engine: The SQLAlchemy database engine.
        """
        engine: Engine = create_engine(
            f"sqlite:///{Config.SQLITE_DB_PATH}",
        )
        return engine

    def get_session(self) -> Session:
        """
        Create a new SQLAlchemy session.
        Returns:
            Session: A new SQLAlchemy session.
        """
        return self.SessionLocal()

    def init_db(self) -> None:
        """
        Initialize the database by creating tables.
        """
        from cryptflows.services.storage.database.models.models import Base, Project, Task 
        Base.metadata.create_all(bind=self.engine)
