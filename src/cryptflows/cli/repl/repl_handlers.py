from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from ...services.workflows.project_management.project_utils import ProjectUtils
from ...services.workflows.project_management.scope_utils import ScopeUtils
from ...app import create_workflows_app
from datetime import datetime
import csv
import logging
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global state
current_scope = None

COMMANDS = {
    "projects": {
        "list": "List all projects",
        "add": "Add a new project",
        "remove": "Remove a project",
    },
    "scope": {
        "set": "Set the current scope",
        "show": "Show the current scope",
    },
    "run": {
        "analysis": "Run analysis on the current scope",
    },
    "help": "Show help message",
    "exit": "Exit the REPL",
}

def parse_command(input_string: str) -> tuple:
    """Parse the input string into main command and sub-command."""
    parts = input_string.strip().lower().split()
    main_command = parts[0] if parts else ""
    sub_command = parts[1] if len(parts) > 1 else ""
    return main_command, sub_command

def run(console: Console, scope: str) -> None:
    """Run the analysis on the given scope."""
    start_time = datetime.now()
    logging.info(f"Running analysis on scope: {scope}")
    console.print(f"[green]Running analysis on scope: {scope}[/green]")
    
    create_workflows_app(scope)

    end_time = datetime.now()
    logging.info(f"Analysis completed. Started at: {start_time}, Finished at: {end_time}")
    console.print(f"[green][bold]All tasks in all projects have been completed.[/bold][/green]")
    console.print(f"[green]Started at: {start_time}[/green]")
    console.print(f"[green]Finished at: {end_time}[/green]")

def scope_csv_to_working_memory(console: Console, scope: str) -> None:
    """Convert scope CSV file to working memory."""
    try:
        with open(scope, 'r') as f:
            reader = csv.DictReader(f)
            scope_list = list(reader)

        for asset in scope_list:
            console.print(asset)
    except FileNotFoundError:
        console.print(f"[red]Error: Scope file '{scope}' not found.[/red]")
    except csv.Error as e:
        console.print(f"[red]Error reading CSV file: {e}[/red]")

def handle_projects(sub_command: str, console: Console) -> None:
    """Handle 'projects' command and its sub-commands."""
    if sub_command == "list":
        projects = ProjectUtils.list_available_projects()
        if projects:
            table = Table(title="Available Projects")
            table.add_column("Project Name", style="cyan")
            for project in projects:
                table.add_row(project)
            console.print(table)
        else:
            console.print("[yellow]No projects found.[/yellow]")
    elif sub_command == "add":
        project_name = Prompt.ask("Enter project name")
        ProjectUtils.create_project(self=None, console=console, name=project_name)
        console.print(f"[green]Project '{project_name}' added successfully.[/green]")
    elif sub_command == "remove":
        project_name = Prompt.ask("Enter project name to remove")
        if ProjectUtils.remove_project(project_name):
            console.print(f"[green]Project '{project_name}' removed successfully.[/green]")
        else:
            console.print(f"[red]Project '{project_name}' not found.[/red]")
    else:
        console.print("Invalid sub-command for 'projects'", style="red bold")

def handle_scope(sub_command: str, console: Console) -> None:
    """Handle 'scope' command and its sub-commands."""
    global current_scope
    if sub_command == "set":
        scope = Prompt.ask("Enter the path to the scope directory")
        ScopeUtils.set_scope(scope)
        current_scope = scope
        console.print(f"[green]Scope set to: {scope}[/green]")
    elif sub_command == "show":
        if current_scope:
            console.print(f"[green]Current scope: {current_scope}[/green]")
        else:
            console.print("[yellow]No scope is currently set.[/yellow]")
    else:
        console.print("Invalid sub-command for 'scope'", style="red bold")

def handle_run(sub_command: str, console: Console) -> None:
    """Handle 'run' command and its sub-commands."""
    global current_scope
    if sub_command == "analysis":
        if not current_scope:
            console.print("[yellow]No scope is set. Please set a scope before running analysis.[/yellow]")
            current_scope = Prompt.ask("Enter the path to the scope directory")
            ScopeUtils.set_scope(current_scope)
        run(console, current_scope)
    else:
        console.print("Invalid sub-command for 'run'", style="red bold")

def show_help(console: Console) -> None:
    """Display help information based on the COMMANDS dictionary."""
    table = Table(title="Available Commands")

    #    Add columns to the table
    table.add_column("Command Category", style="bold", no_wrap=True)
    table.add_column("Sub-command", style="bold")
    table.add_column("Description")

    # Add rows to the table
    for category, subcommands in COMMANDS.items():
        if isinstance(subcommands, dict):
            for subcommand, description in subcommands.items():
                table.add_row(category, subcommand, description)
        else:
            table.add_row(category, "-", subcommands)

    # Print the table
    console.print(table)

def repl(console: Console, session: Session) -> None:
    """
    Main REPL (Read-Eval-Print Loop) function for the CryptFlows framework.
    
    This function provides a command-line interface for users to interact with various
    features of the CryptFlows framework, including project management, scope setting,
    and analysis running.

    Args:
        console (Console): Rich console object for formatted output.

    Returns:
        None
    """
    console.print("[bold green]Welcome to Cryptflows REPL[/bold green]")
    console.print("Type 'help' for a list of commands.")

    while True:
        try:
            input_string: str = Prompt.ask("[bold blue]>>>[/bold blue]")
            main_command, sub_command = parse_command(input_string)

            if main_command == "exit":
                console.print("[bold red]Exiting REPL...[/bold red]")
                break
            elif main_command == "help":
                show_help(console)
            elif main_command == "projects":
                handle_projects(sub_command, console)
            elif main_command == "scope":
                handle_scope(sub_command, console)
            elif main_command == "run":
                handle_run(sub_command, console)
            else:
                console.print("Invalid command. Type 'help' for a list of commands.", style="red bold")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            console.print(f"[red]An error occurred: {e}[/red]")

