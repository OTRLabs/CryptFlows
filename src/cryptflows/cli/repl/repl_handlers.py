from rich.console import Console
from rich.prompt import Prompt
from ...services.storage.projects.db_utils import list_available_projects
import csv

from .repl_utils import COMMANDS

from ...app import create_workflows_app

from datetime import datetime
def run(console: Console, scope: str):
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
    
    
    # Print a message to indicate that the analysis is running on the given scope
    console.print(f"[green]Running analysis on scope: {scope}[/green]")
    
    # Create the workflows application for the given scope
    create_workflows_app(scope)

    # Print a message to indicate that all tasks in all projects have been completed
    console.print(f"[green][bold]All tasks in all projects have been completed.[/bold][/green]\n\n\n[green]Started at: {start_time}\n[/green][green]Finished at: {datetime.now()}[/green]")




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

def handle_projects(sub_command: str, console: Console) -> None:
    if sub_command == "list":
        console.print("Listing all projects...")
        projects_in_storage = list_available_projects()
        # Display projects_in_storage
    elif sub_command == "add":
        project_name = Prompt.ask("Enter project name")
        # Add project logic here
    elif sub_command == "remove":
        project_name = Prompt.ask("Enter project name to remove")
        # Remove project logic here
    else:
        console.print("Invalid sub-command for 'projects'", style="red bold")

def handle_scope(sub_command: str, console: Console) -> None:
    if sub_command == "set":
        scope = Prompt.ask("Enter the path to the scope directory")
        scope_csv_to_working_memory(scope=scope)
    elif sub_command == "show":
        # Logic to show current scope
        pass
    else:
        console.print("Invalid sub-command for 'scope'", style="red bold")

def handle_run(sub_command: str, console: Console) -> None:
    if sub_command == "analysis":
        scope = Prompt.ask("Enter the path to the scope directory")
        run(scope=scope)
    else:
        console.print("Invalid sub-command for 'run'", style="red bold")

def show_help(console: Console) -> None:
    console.print("[bold yellow]Available commands:[/bold yellow]")
    for command, details in COMMANDS.items():
        if isinstance(details, dict):
            console.print(f"  {command}:")
            for sub_command, description in details.items():
                console.print(f"    - {sub_command}: {description}")
        else:
            console.print(f"  {command}: {details}")




def repl(console: Console, scope: str) -> None:
    """
    This function is the main entry point of the REPL (Read-Eval-Print Loop) application. It provides a command-line interface for users to interact with the CryptFlows framework.

    Args:
        None

    Returns:
        None
    """
    
    console.print("[bold green]Cryptflows REPL[/bold green]")

    while True:
        command: str = Prompt.ask("[bold blue]>>>[/bold blue]").strip().lower()

        if command == "exit":
            console.print("[bold red]Exiting REPL...[/bold red]")
            break
        elif command == "help":
            console.print("[bold yellow]Available commands:[/bold yellow]")
            console.print("  run - Run analysis on a scope")
            console.print("  scope - Enter the path to the scope directory")
            console.print("  projects - List all projects in the database")
            console.print("  help - Show this help message")
            console.print("  exit - Exit the REPL")
        elif command == "run":
            scope: str = Prompt.ask("[bold blue]Enter the path to the scope directory[/bold blue]")
            run(scope=scope)
        
        elif command == "scope":
            scope: str = Prompt.ask("[bold blue]Enter the path to the scope directory[/bold blue]")
            scope_csv_to_working_memory(scope=scope)

        elif command == "projects":
            console.print("All projects in the database", style="yellow bold")
            
            projects_in_storage: list = list_available_projects()
            
        else:
            console.print("Invalid command. Please try again.", style="red bold")
