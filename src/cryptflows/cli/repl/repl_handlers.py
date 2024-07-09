from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from typing import Dict, Callable, Any
import csv
import logging
from sqlalchemy.orm import Session
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

from ...services.workflows.project_management.project_utils import ProjectUtils
from ...services.workflows.project_management.scope_utils import ScopeUtils
from ...app import create_workflows_app

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptFlowsREPL:
    def __init__(self, console: Console, db_session: Session):
        self.console = console
        self.db_session = db_session
        self.current_scope = None
        self.commands: Dict[str, Dict[str, Callable]] = {}
        self.register_commands()

    def register_commands(self):
        """Register all available commands."""
        self.register_command("projects", "list", self.list_projects, "List all projects")
        self.register_command("projects", "add", self.add_project, "Add a new project")
        self.register_command("projects", "remove", self.remove_project, "Remove a project")
        self.register_command("scope", "set", self.set_scope, "Set the current scope")
        self.register_command("scope", "show", self.show_scope, "Show the current scope")
        self.register_command("run", "analysis", self.run_analysis, "Run analysis on the current scope")
        self.register_command("help", None, self.show_help, "Show help message")
        self.register_command("exit", None, self.exit_repl, "Exit the REPL")

    def register_command(self, main_command: str, sub_command: str, func: Callable, description: str):
        """Register a command with the REPL."""
        if main_command not in self.commands:
            self.commands[main_command] = {}
        self.commands[main_command][sub_command or '__main__'] = {
            'func': func,
            'description': description
        }

    def parse_command(self, input_string: str) -> tuple:
        """Parse the input string into main command and sub-command."""
        parts = input_string.strip().lower().split()
        main_command = parts[0] if parts else ""
        sub_command = parts[1] if len(parts) > 1 else ""
        return main_command, sub_command

    def run_analysis(self):
        """Run the analysis on the current scope."""
        if not self.current_scope:
            self.console.print("[yellow]No scope is set. Please set a scope before running analysis.[/yellow]")
            self.set_scope()
        
        if self.current_scope:
            create_workflows_app(self.current_scope)
            self.console.print(f"[green]Analysis completed for scope: {self.current_scope}[/green]")

    def list_projects(self):
        """List all available projects."""
        projects = ProjectUtils.list_available_projects(self.db_session)
        if projects:
            table = Table(title="Available Projects")
            table.add_column("Project Name", style="cyan")
            for project in projects:
                table.add_row(project)
            self.console.print(table)
        else:
            self.console.print("[yellow]No projects found.[/yellow]")

    def add_project(self):
        """Add a new project."""
        project_name: str = Prompt.ask("Enter project name")
        ProjectUtils.create_project(self.console, name=project_name, session=self.db_session)
        self.current_scope = project_name
        self.console.print(f"[green]Project '{project_name}' added successfully.[/green]")
        self.console.print(f"[green]Current scope set to: {self.current_scope}[/green]")

    def remove_project(self):
        """Remove a project."""
        project_name = Prompt.ask("Enter project name to remove")
        if ProjectUtils.remove_project(project_name, self.db_session):
            self.console.print(f"[green]Project '{project_name}' removed successfully.[/green]")
        else:
            self.console.print(f"[red]Project '{project_name}' not found.[/red]")

    def set_scope(self):
        """Set the current scope."""
        scope = Prompt.ask("Enter the path to the scope directory")
        ScopeUtils.set_scope(scope)
        self.current_scope = scope
        self.console.print(f"[green]Scope set to: {scope}[/green]")

    def show_scope(self):
        """Show the current scope."""
        if self.current_scope:
            self.console.print(f"[green]Current scope: {self.current_scope}[/green]")
        else:
            self.console.print("[yellow]No scope is currently set.[/yellow]")

    def show_help(self):
        """Display help information based on the registered commands."""
        table = Table(title="Available Commands")
        table.add_column("Command", style="bold", no_wrap=True)
        table.add_column("Sub-command", style="bold")
        table.add_column("Description")

        for main_command, subcommands in self.commands.items():
            for sub_command, details in subcommands.items():
                sub_command_str = sub_command if sub_command != '__main__' else '-'
                table.add_row(main_command, sub_command_str, details['description'])

        self.console.print(table)

    def exit_repl(self):
        """Exit the REPL."""
        self.console.print("[bold red]Exiting REPL...[/bold red]")
        raise SystemExit

    def run(self):
        """Run the REPL."""
        self.console.print("[bold green]Welcome to Cryptflows REPL[/bold green]")
        self.console.print("Type 'help' for a list of commands.")

        # Create a prompt session with auto-completion
        command_completer = WordCompleter(list(self.commands.keys()))
        session = PromptSession(completer=command_completer)

        while True:
            try:
                input_string = session.prompt(">>> ", style="bold blue")
                main_command, sub_command = self.parse_command(input_string)

                if main_command in self.commands:
                    if sub_command in self.commands[main_command] or '__main__' in self.commands[main_command]:
                        command = self.commands[main_command].get(sub_command) or self.commands[main_command]['__main__']
                        command['func']()
                    else:
                        self.console.print(f"Invalid sub-command for '{main_command}'. Type 'help' for available commands.", style="red bold")
                else:
                    self.console.print("Invalid command. Type 'help' for a list of commands.", style="red bold")
            except SystemExit:
                break
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                self.console.print(f"[red]An error occurred: {e}[/red]")

def init_repl(console: Console, db_session: Session):
    repl = CryptFlowsREPL(console, db_session)
    repl.run()
