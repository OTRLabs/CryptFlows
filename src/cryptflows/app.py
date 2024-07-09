from __future__ import annotations
from rich import print
import asyncio
import logging
from rich.console import Console
from .configs.config import Config
from .services.workflows.project_management.project_utils import init_project_db_session
from .services.workflows.tasking.tasking_utils import send_task, consume_task

def initialize_application_services(console: Console) -> None:
    """
    Initializes the application services.

    This function initializes the project database session and prints a message indicating that projects
    can be created in the database. It also prints a message indicating that tasks to be completed from
    a previous run need to be implemented.

    :return: None
    """
    console.print("Initializing project database session...", style="bold green")
    init_project_db_session()
    console.print("Project database session initialized. Projects can be created in the database.", style="bold green")

    # TODO: Implement checking for existing tasks that need completion from a previous run
    console.print("Initializing workflows application...", style="bold green")

    

def create_workflows_app(console: Console, scope: str) -> None:
    print("[green]Initializing application...[/green]")
    
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    print(f"[green]Logger level: {logging.getLevelName(logger.level)}[/green]")

    # Initialize the application services
    initialize_application_services()

    print("[green]Creating workflows application...[/green]")
    
    # Example task and host
    example_task = {
        "queue": "example_queue",
        "body": {"message": "Hello, World!"}
    }
    example_host = {"host": "localhost"}

    # Send and consume tasks
    asyncio.run(send_task(example_task, example_host))
    asyncio.run(consume_task(example_task, example_host))


