from __future__ import annotations
from cryptflows.app import create_workflows_app
from cryptflows.services.workflows.project_management.project_utils import Project
from datetime import datetime
from rich.console import Console, Theme
from rich.prompt import Prompt
import csv
from cryptflows.cli.repl.repl_utils import COMMANDS
from cryptflows.cli.repl.repl_handlers import CryptFlowsREPL, init_repl
from advanced_alchemy.repository import SQLAlchemySyncRepository
from cryptflows.services.storage.database.db import DatabaseUtils
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cryptflows.configs.config import Config
from cryptflows.services.storage.database.models.models import Base


def main() -> None:
    """
    This is the main entry point of the CLI application. 

    """
    ## init the application's rich console
    console: Console = Console(stderr=True, theme=Theme({"repl": "bold green"}))

    console.print("CryptFlows", style="bold green")
    console.print(f"Initializing at {datetime.now()}...")

    #Base = declarative_base
    console.print(f"Base: {Base}")
    db_engine = create_engine(Config.SQLITE_DB_PATH)
    # connect to all application services
    database_utils = DatabaseUtils(console=console, engine=db_engine)
    ## check if the sqlite database exists
    
    session = database_utils.get_session()

    console.print(f"Connected to database at {datetime.now()}...")
    console.print(f"Initialized at {datetime.now()}...")
    

    # Example: Fetching projects
    #projects = database_utils.get_projects()
    #console.print(f"Projects: {projects}")

    
    console.print(f"Launching REPL at {datetime.now()}...")

    init_repl(console=console, db_session=session)
    
if __name__ == "__main__":
    main()
