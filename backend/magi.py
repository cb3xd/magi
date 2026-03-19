from enum import Enum
from typing import Dict, List, Literal, cast
from pathlib import Path
from groq.types.chat import ChatCompletionMessageParam
from backend.models import Message, MagiState
from groq import Groq
from dotenv import load_dotenv
import os


class MagiUnit(Enum):
    Melchior = (
        'qwen/qwen3-32b',
        (Path('prompts') / 'Melchior.txt').read_text(encoding='utf-8'),
    )
    Balthasar = (
        'qwen/qwen3-32b',
        (Path('prompts') / 'Balthasar.txt').read_text(encoding='utf-8'),
    )
    Casper = (
        'qwen/qwen3-32b',
        (Path('prompts') / 'Casper.txt').read_text(encoding='utf-8'),
    )

    def __init__(self, model: str, base_prompt: str):
        load_dotenv()
        api_key = os.getenv('API_KEY')
        print(api_key)
        self.client = Groq(api_key=api_key)
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
    def ask(self, prompt: str):
        for unit in MagiUnit:
            print(f'[{unit.name}]')
            unit.add_message('user', prompt)
            unit.send_messages()
            print(f'[{unit.name}]')
