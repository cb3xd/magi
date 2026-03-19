import asyncio
from textual.app import App, ComposeResult
from textual.widgets import Input, Static
from textual.containers import Horizontal
from rich.panel import Panel
from rich.text import Text
from frontend import MagiNode
from frontend.styles import DIM_CYAN, RED, CYAN, AMBER


class MagiApp(App):
    def compose(self) -> ComposeResult:
        header_text = Text.assemble(
            ('DIRECT LINK CONNECTION: MAGI 01\n', f'bold {AMBER}'),
        )
        yield Static(Panel(header_text, border_style=AMBER), id='header')

        # Yield our custom node objects
        with Horizontal(id='node-container'):
            yield MagiNode('CASPER-3', id='node_c')
            yield MagiNode('BALTHASAR-2', id='node_b')
            yield MagiNode('MELCHIOR-1', id='node_m')

        # Yield the built-in interactive input field
        yield Input(placeholder='AWAITING SYSTEM COMMAND...', id='cli_input')

    async def on_mount(self) -> None:
        self.query_one(Input).focus()
        asyncio.create_task(self.simulate_backend_signals())

    async def simulate_backend_signals(self):
        await asyncio.sleep(1)

        boot_sequence = ['node_m', 'node_b', 'node_c']

        for node_id in boot_sequence:
            node = self.query_one(f'#{node_id}', MagiNode)

            # Waking Phase
            node.status = 'WAKING'
            node.color = AMBER
            await asyncio.sleep(0.8)

            # Online Phase
            node.status = 'ONLINE'
            node.color = CYAN
            await asyncio.sleep(0.5)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        command = event.value.strip().upper()
        input_widget = self.query_one(Input)

        input_widget.value = ''

        if command == 'OVERRIDE':
            for node in self.query(MagiNode):
                node.status = 'REJECT'
                node.color = RED
        elif command == 'REBOOT':
            for node in self.query(MagiNode):
                node.status = 'OFFLINE'
                node.color = 'white'
            asyncio.create_task(self.simulate_backend_signals())
        elif command == 'QUIT' or command == 'EXIT':
            self.exit()
