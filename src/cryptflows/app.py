from __future__ import annotations
from rich import print
import asyncio

from .configs.config import Config

from .workflows.tasking.tasking_utils import send_task, consume_task

def create_workflows_app():
    
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
