from __future__ import annotations
from rich import print
import asyncio
import logging
from .configs.config import Config
from .workflows.project_management.project_utils import init_project_db_session
from .workflows.tasking.tasking_utils import send_task, consume_task


def initialize_application_services() -> None:
    print("[green]Initializing project database session...[/green]")
    init_project_db_session()
    print(f"[green]Project database session initialized\n\nProject's can be created in the database[/green]")

    # TODO: Implement checking to see if there are any existing tasks in any projects that need to be completed from a previous run

    print("[green]Initializing workflows application...[/green]")

    # connect to the main database

    
def create_workflows_app(scope: str) -> None:

    print("[green]Initializing application...[/green]")
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    print(f"[green]Logger level: {logging.getLevelName(logger.level)}[/green]")
    
    

    print(f"[green]Initializing workflows application[/green]")
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
