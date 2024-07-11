

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
    parts = input_string.strip().lower().split()
    main_command = parts[0] if parts else ""
    sub_command = parts[1] if len(parts) > 1 else ""
    return main_command, sub_command