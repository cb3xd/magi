from textual.widgets import Static
from textual.reactive import reactive
from rich.panel import Panel
from rich.text import Text
from rich.align import Align


class MagiNode(Static):
    status = reactive('OFFLINE')
    color = reactive('white')

    def __init__(self, name: str, code: str = '258', **kwargs):
        super().__init__(**kwargs)
        self.node_name = name
        self.code = code

    def render(self) -> Panel:
        kanji = (
            ' 承認 '
            if self.status == 'ONLINE'
            else (' 拒絶 ' if self.status == 'REJECT' else ' 待機 ')
        )
        if self.status == 'OFFLINE':
            kanji = ' ---- '

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
