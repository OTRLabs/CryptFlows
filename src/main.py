from __future__ import annotations
#import rich_click as click
from cryptflows.app import create_workflows_app
from cryptflows.services.workflows.project_management.project_utils import Project
from datetime import datetime
from rich.console import Console, Theme
#from litestar import Litestar
#import rich_click as click
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt
import csv
from cryptflows.cli.repl.repl_utils import COMMANDS
from cryptflows.cli.repl.repl_handlers import CryptFlowsREPL, init_repl
#from cryptflows.app import init_sqlite_project_db_service_session
#from cryptflows.services.storage.projects.scope_utils import ask_use
from cryptflows.services.storage.database.db import connect_to_database
from advanced_alchemy.repository import SQLAlchemySyncRepository

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

    #    session = connect_to_database()
    
    console.print(f"Connected to database at {datetime.now()}...")
    console.print(f"Initialized at {datetime.now()}...")
    
    console.print(f"Launching REPL at {datetime.now()}...")
    init_repl(console=console, db_session=session)
    
    
    
    
if __name__ == "__main__":
    
    main()