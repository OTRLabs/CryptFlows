from __future__ import annotations

from .....configs.config import Config
from rich import Console
from rich.columns import Columns
import ollama


def init_ollama():
    pass


def get_list_of_models_from_ollama(console: Console, config: Config) -> list:
    
    list_of_models: list = ollama.list()
    console.print("[bold green]Available models:[/bold green]")
    console.print(Columns(list_of_models), style="green")
    return list_of_models

async def prompt_an_ollama_model(console: Console, config: Config) -> str:
    pass