
import os

from rich.console import Console
from rich.prompt import Prompt
class ScopeUtils:
    def ask_user_for_scope(console: Console) -> str:
        scope: str = Prompt.ask(
            "Enter the path to the scope directory",
        )

        return scope

    def scope_exists(console: Console) -> bool:
        scope = ask_user_for_scope(console)
        if os.path.exists(scope):
            return True
        else:
            return False

    def set_scope(scope: str) -> None:
        os.environ["SCOPE"] = scope
        console = Console()
        console.print(f"Scope set to: {scope}")

    def get_current_scope(scope: str) -> str:
        return scope