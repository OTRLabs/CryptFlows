from __future__ import annotations
import rich_click as click
from cryptflows.app import create_workflows_app, initialize_application_services
from datetime import datetime
from rich.console import Console
#from litestar import Litestar



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
    
    # Initialize the application services. This step initializes the project database session and
    # prints a message indicating that projects can be created in the database. It also prints a
    # message indicating that tasks to be completed from a previous run need to be implemented.
    with console.status("[bold green]Initializing application...[/bold green]") as status:
        while not status.is_finished:
            status.update("Initializing application...")
            initialize_application_services()
    
        console.log("[green]Application initialized. Projects can be created in the database.[/green]")
        
    # Create the workflows application for the given scope
    create_workflows_app(scope)

    # Print a message to indicate that all tasks in all projects have been completed
    click.echo(f"[green][bold]All tasks in all projects have been completed.[/bold][/green]\n\n\n[green]Started at: {start_time}\n[/green][green]Finished at: {datetime.now()}[/green]")


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