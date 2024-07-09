


from rich.console import Console
from rich.prompt import Prompt

def ask_user_for_scope(console: Console) -> str:
    scope: str = Prompt.ask(
        "Enter the path to the scope directory",
    )

    return scope