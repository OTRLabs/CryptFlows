from __future__ import annotations
import rich_click as click
from cryptflows.app import create_workflows_app, initialize_application_services

from datetime import datetime
from rich.console import Console
#from litestar import Litestar
import rich_click as click
from cryptflows.app import create_workflows_app, initialize_application_services
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt
import csv

console = Console()
import csv


def scope_csv_to_working_memory(scope: str) -> None:
    """
    This function takes a scope CSV file and converts it into a working memory. The scope CSV file contains
    the assets to be analyzed. The scope CSV file is a CSV file that contains the following columns:
    - id: The ID of the asset. This is used to identify the asset in the scope CSV file.
    - name: The name of the asset. This is used to identify the asset in the scope CSV file.
    - type: The type of the asset. This is used to identify the asset in the scope CSV file.
    - value: The value of the asset. This is used to identify the asset in the scope CSV file.

    Args:
        scope (str): The path to the scope CSV file.

    Returns:
        None
    """
    # Read the scope CSV file into a list of dictionaries
    with open(scope, 'r') as f:
        reader = csv.DictReader(f)
        scope_list = list(reader)

    # Convert the list of dictionaries into a working memory
    for asset in scope_list:
        print(asset)

    return

def run(scope: str):
    """
    This is the main entry point of the CLI application. It takes a scope as input and runs the analysis
    on that scope. The scope is a directory that contains the assets to be analyzed.

    Args:
        scope (str): The path to the scope directory.

    Returns:
        None
    """
    # Record the start time of the analysis
    start_time = datetime.now()
    
    # Create a console object to print messages to the user
    console = Console()
    
    # Print a message to indicate that the analysis is running on the given scope
    console.print(f"[green]Running analysis on scope: {scope}[/green]")
    
    console.print
    # Create the workflows application for the given scope
    create_workflows_app(scope)

    # Print a message to indicate that all tasks in all projects have been completed
    click.echo(f"[green][bold]All tasks in all projects have been completed.[/bold][/green]\n\n\n[green]Started at: {start_time}\n[/green][green]Finished at: {datetime.now()}[/green]")


def repl():
    console.print("[bold green]Cryptflows REPL[/bold green]")

    while True:
            command = Prompt.ask("[bold blue]>>>[/bold blue]").strip().lower()

            if command == "exit":
                console.print("[bold red]Exiting REPL...[/bold red]")
                break
            elif command == "help":
                console.print("[bold yellow]Available commands:[/bold yellow]")
                console.print("  run - Run analysis on a scope")
                console.print("  scope - Enter the path to the scope directory")
                console.print("  help - Show this help message")
                console.print("  exit - Exit the REPL")
            elif command == "run":
                scope = Prompt.ask("[bold blue]Enter the path to the scope directory[/bold blue]")
                run(scope=scope)
            
            elif command == ""
            

def main() -> None:
    """
    This is the main entry point of the CLI application. It takes a scope as input and runs the analysis
    on that scope. The scope is a directory that contains the assets to be analyzed.

    Args:
        scope (str): The path to the scope directory.

    Returns:
        None
    """

    scope: str = click.prompt(
        "Enter the path to the scope directory",
        type=click.Path(exists=True),
    )
    
    
    run(scope=scope)
    
    
    
    
if __name__ == "__main__":
    main()