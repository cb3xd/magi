from textual.widgets import Static
from textual.reactive import reactive
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from backend import MagiState


class MagiNode(Static):
    status = reactive('OFFLINE')
    color = reactive('white')

    def __init__(self, name: str, code: str, **kwargs):
        super().__init__(**kwargs)
        self.node_name = name
        self.code = code

    def render(self) -> Panel:
        kanji = ' 遊休 '
        if self.status == MagiState.THINKING:
            kanji = ' 思索 '

        content = Text.assemble(
            (f'\n{self.node_name}\n', f'bold {self.color}'),
            (
                f'{kanji}',
                f'reverse bold {self.color}'
                if self.status != 'OFFLINE'
                else 'dim',
            ),
        )

        return Panel(
            Align.center(content),
            title=f'[dim]CODE: {self.code}[/]',
            title_align='left',
            border_style=self.color
            if self.status != 'OFFLINE'
            else 'dim white',
            padding=(1, 2),
        )
