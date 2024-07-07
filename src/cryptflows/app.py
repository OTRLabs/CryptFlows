from __future__ import annotations
from rich import print
import asyncio
import logging
from .configs.config import Config

from .workflows.tasking.tasking_utils import send_task, consume_task

def create_workflows_app(scope: str) -> None:
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    print(f"[green]Logger level: {logging.getLevelName(logger.level)}[/green]")
    
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
