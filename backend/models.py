from enum import Enum
from typing import TypedDict


class MagiState(str, Enum):
    IDLE = 'idle'
    THINKING = 'thinking'


class Message(TypedDict):
    role: str
    content: str
