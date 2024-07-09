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

from rich.console import Console
from sqlalchemy.orm import Session
from .services.workflows.project_management.project_utils import ProjectUtils

def initialize_application_services(console: Console) -> Session:
    """
    Initializes the application services.

    This function initializes the project database session and prints a message indicating that projects
    can be created in the database. It also prints a message indicating that tasks to be completed from
    a previous run need to be implemented.

    :param console: Console object for printing messages of type Console
    :return: Session object representing the project database session of type Session
    """
    console.print("Initializing workflows application...", style="bold green")

    session: Session = ProjectUtils.init_project_db_session(self=ProjectUtils(), console=console)

    return session


def init_sqlite_project_db_service_session(console: Console) -> Session:
    '''
    returns a session allowing you to use sqlalchemy to read & write to the sqlite database
    '''
    console.print("Initializing connection to the applications sqlite database...", style="bold green")
    session: Session = ProjectUtils.init_project_db_session(console=console)

    return session


def create_workflows_app(console: Console, scope: str) -> None:
    """
    Initializes the workflows application.

    :param console: Console object for printing messages
    :param scope: A string indicating the scope
    :return: None
    """
    print("[green]Initializing application...[/green]")
    
    # Configure logging
    console.print("Configuring logging...", style="bold green")

    # Initialize the application services
    initialize_application_services()

    console.print("Creating workflows application...", style="bold green")
    
    # Example task and host
    example_task: dict = {
        "queue": "example_queue",
        "body": {"message": "Hello, World!"}
    }
    example_host: dict = {"host": "localhost"}

    # Send and consume tasks
    asyncio.run(send_task(example_task, example_host))
    asyncio.run(consume_task(example_task, example_host))


