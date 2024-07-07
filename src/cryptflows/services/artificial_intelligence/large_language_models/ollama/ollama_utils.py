from __future__ import annotations

from .....configs.config import Config
from rich import Console
from rich.columns import Columns
import ollama


def init_ollama():
    """
    This function initializes the ollama http server.
    It creates a new server instance if the server is not already running.
    The server is initialized with a port and an endpoint.
    The function also starts the server.
    """
    # TODO: Implement the code for initializing the ollama http server
    pass


def get_list_of_models_from_ollama(console: Console, config: Config) -> list:
    
    list_of_models: list = ollama.list()
    console.print("[bold green]Available models:[/bold green]")
    console.print(Columns(list_of_models), style="green")
    return list_of_models


async def select_an_ollama_model(console: Console, config: Config,task: dict, list_of_models: list) -> str:
    '''
    this function is used to select the right ollama model for a specific task.
    first it assesses the task, and then selects the right model.
    it analyzes the list_of_models we have available, and returns a string that is the value of the name of the right (or really, best) model name for the task.
    '''
    
    
    
    pass

async def prompt_an_ollama_model(console: Console, config: Config, model_name: str) -> str:
    pass