
import os

from rich.console import Console
from rich.prompt import Prompt
class ScopeUtils:

    def __init__(self):
        pass

    def ask_user_for_scope(self, console: Console) -> str:
        scope: str = Prompt.ask(
            "Enter the path to the scope directory",
        )

        return scope

    def scope_exists(self, console: Console) -> bool:
        scope = self.ask_user_for_scope(console)
        if os.path.exists(scope):
            return True
        else:
            return False

    def set_scope(self, console: Console, scope: str) -> None:
        os.environ["SCOPE"] = scope
        console = Console()
        console.print(f"Scope set to: {scope}")

    def get_current_scope(self, scope: str) -> str:
        # TODO: OPTIMIZE this to actually get the current scope somehow
        return scope