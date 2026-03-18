from typing import List
from pathlib import Path
from backend.models import Message, MagiState


class MagiUnit:
    def __init__(self, name: str, model: str, base_prompt: str):
        self.name = name
        self.model = model
        self.messages: List[Message] = []
        self.add_message('system', base_prompt)
        self.state = MagiState.IDLE

    def add_message(self, role: str, content: str) -> None:
        message: Message = {'role': role, 'content': content}
        self.messages.append(message)


class Magi:
    def __init__(self):
        unit_names = ['Melchior', 'Casper', 'Balthasar']
        self.units = {}
        for unit_name in unit_names:
            prompt_path = Path('prompts') / f'{unit_name}.txt'
            prompt = prompt_path.read_text(encoding='utf-8')
            magi_unit = MagiUnit(unit_name, 'qwen3-32b', prompt)
            self.units[unit_name] = magi_unit
