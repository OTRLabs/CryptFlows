

from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, ContentSwitcher, DataTable, Markdown
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static
class CryptFlowsApp(App):

    #BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]


    def compose(self) -> ComposeResult:
        yield Header()
        
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    
