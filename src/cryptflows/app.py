from __future__ import annotations
from rich import print
import asyncio
import logging
from rich.console import Console
from .configs.config import Config
from .services.workflows.project_management.project_utils import ProjectUtils
from .services.workflows.tasking.tasking_utils import send_task, consume_task
from sqlalchemy.orm import Session


from rich.console import Console
from .services.workflows.project_management.project_utils import ProjectUtils

def initialize_application_services(console: Console) -> Session:
    """
    Initializes the application services.

    This function initializes the project database session and prints a message indicating that projects
    can be created in the database. It also prints a message indicating that tasks to be completed from
    a previous run need to be implemented.

    :param console: Console object for printing messages
    :return: Session object representing the project database session
    """
    console.print("Initializing workflows application...", style="bold green")

    project_utils = ProjectUtils()
    session: Session = project_utils.init_project_db_session()

    return session

    

def create_workflows_app(console: Console, scope: str) -> None:
    print("[green]Initializing application...[/green]")
    
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    print(f"[green]Logger level: {logging.getLevelName(logger.level)}[/green]")

    # Initialize the application services
    initialize_application_services()

    console.print("Creating workflows application...", style="bold green")
    
    # Example task and host
    example_task = {
        "queue": "example_queue",
        "body": {"message": "Hello, World!"}
    }
    example_host = {"host": "localhost"}

    # Send and consume tasks
    asyncio.run(send_task(example_task, example_host))
    asyncio.run(consume_task(example_task, example_host))


