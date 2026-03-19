import asyncio
from textual.app import App, ComposeResult
from textual.widgets import Input, Static
from textual.containers import Horizontal
from rich.panel import Panel
from rich.text import Text
from backend import MagiState
from frontend import MagiNode
from frontend.styles import AMBER, CD_CSS, CYAN


class MagiApp(App):
    CSS = CD_CSS

    def compose(self) -> ComposeResult:
        header_text = Text.assemble(
            ('DIRECT LINK CONNECTION: MAGI 01\n', f'bold {AMBER}'),
        )
        yield Static(Panel(header_text, border_style=AMBER), id='header')

        # Yield our custom node objects
        with Horizontal(id='node-container'):
            yield MagiNode('CASPER-3', id='node_c', code='401')
            yield MagiNode('BALTHASAR-2', id='node_b', code='401')
            yield MagiNode('MELCHIOR-1', id='node_m', code='401')

        # Yield the built-in interactive input field
        yield Input(placeholder='AWAITING SYSTEM COMMAND...', id='cli_input')

    def on_input_submitted(self, event: Input.Submitted) -> None:
        command = event.value.strip().upper()
        input_widget = self.query_one(Input)

        input_widget.value = ''

        if command == 'BOOT':
            for node in self.query(MagiNode):
                node.status = MagiState.IDLE
                node.color = CYAN
                node.code = '200'
        elif command == 'QUIT' or command == 'EXIT':
            self.exit()
