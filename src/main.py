from __future__ import annotations
#import rich_click as click
from cryptflows.app import create_workflows_app
from cryptflows.services.storage.projects.project_db import Session, Project
from cryptflows.services.storage.projects.db_utils import list_available_projects
from datetime import datetime
from rich.console import Console, Theme
#from litestar import Litestar
#import rich_click as click
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt
import csv
from cryptflows.cli.repl.repl_utils import COMMANDS
from cryptflows.cli.repl.repl_handlers import run, repl
from cryptflows.app import initialize_application_services
#from cryptflows.services.storage.projects.scope_utils import ask_user_for_scope


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
    initialize_application_services()
    # connect to all application services


    console.print(f"Initialized at {datetime.now()}...")
    
    console.print(f"Launching REPL at {datetime.now()}...")
    repl(console=console)
    
    
    
    
if __name__ == "__main__":
    
    main()