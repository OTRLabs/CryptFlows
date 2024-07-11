from time import monotonic
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static
from textual.reactive import reactive
from cryptflows.services.workflows.project_management.project_utils import ProjectUtils

class ProjectManagementDisplay(ScrollableContainer):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "add":
            ProjectUtils.()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

