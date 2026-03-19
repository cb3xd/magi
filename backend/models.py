from enum import Enum
from typing import Literal, TypedDict


class MagiState(str, Enum):
    IDLE = 'idle'
    THINKING = 'thinking'


class Message(TypedDict):
    role: Literal['system', 'user', 'assistant']
    content: str
