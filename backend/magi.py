from typing import List, Literal, cast
from pathlib import Path

from groq.types.chat import ChatCompletionMessageParam
from backend.models import Message, MagiState
from groq import Groq
from dotenv import load_dotenv
import os


class MagiUnit:
    def __init__(self, name: str, model: str, base_prompt: str):
        load_dotenv()
        api_key = os.getenv('API_KEY')
        print(api_key)
        self.client = Groq(api_key=api_key)
        self.name = name
        self.model = model
        self.messages: List[Message] = []
        self.add_message('system', base_prompt)
        self.state = MagiState.IDLE

    def add_message(
        self, role: Literal['user', 'system', 'assistant'], content: str
    ) -> None:
        message: Message = {'role': role, 'content': content}
        self.messages.append(message)

    def send_messages(self):
        msgs = cast(list[ChatCompletionMessageParam], self.messages)
        try:
            self.completion = self.client.chat.completions.create(
                messages=msgs,
                model=self.model,
                temperature=0.1,
                stream=True,
                reasoning_effort='none',
            )
            self.response_stream()
        except Exception as e:
            print(f'CRITICAL ERROR: {e}')

    def response_stream(self):
        for chunk in self.completion:
            content = chunk.choices[0].delta.content or ''
            print(content, end='', flush=True)


class Magi:
    def __init__(self):
        unit_names = ['Melchior', 'Casper', 'Balthasar']
        self.units = {}
        for unit_name in unit_names:
            prompt_path = Path('prompts') / f'{unit_name}.txt'
            prompt = prompt_path.read_text(encoding='utf-8')
            magi_unit = MagiUnit(unit_name, 'qwen/qwen3-32b', prompt)
            self.units[unit_name] = magi_unit
