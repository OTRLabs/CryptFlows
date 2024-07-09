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

def main() -> None:
    """
    This is the main entry point of the CLI application. It takes a scope as input and runs the analysis
    on that scope. The scope is a directory that contains the assets to be analyzed.

    Args:
        scope (str): The path to the scope directory.

    Returns:
        None
    """
    ## init the application's rich console
    console: Console = Console(stderr=True, theme=Theme({"repl": "bold green"}))

    console.print("CryptFlows", style="bold green")
    console.print(f"Initializing at {datetime.now()}...")

    # connect to all application services
    database_utils = DatabaseUtils(console=console)
    database_utils.init_db()  # Initialize the database and create tables
    session = database_utils.get_session()

    console.print(f"Connected to database at {datetime.now()}...")
    console.print(f"Initialized at {datetime.now()}...")
    
    console.print(f"Launching REPL at {datetime.now()}...")
    init_repl(console=console, db_session=session)
    
if __name__ == "__main__":
    main()
