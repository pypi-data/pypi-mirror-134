from __future__ import annotations

import enum
from typing import TypeVar, Coroutine, Any, Union, Type

T = TypeVar('T')

Coro = Coroutine[Any, Any, T]


class CommandOptionType(enum.Enum):
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8
    MENTIONABLE = 9
    NUMBER = 10
