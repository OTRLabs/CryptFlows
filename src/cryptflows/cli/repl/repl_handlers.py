from rich.console import Console
from rich.prompt import Prompt
from ...services.storage.projects.db_utils import list_available_projects


from .repl_utils import COMMANDS


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