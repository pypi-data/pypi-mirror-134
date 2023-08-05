from __future__ import annotations
import asyncio
from typing import Any, Optional, Callable, TYPE_CHECKING, TypeVar

import discord
from typing_extensions import Concatenate, ParamSpec

from discord import Client

from .context import ContextT
from .types import Coro
from .command import Command
from discord.ext.commands import dm_only, Bot


if TYPE_CHECKING:
    P = ParamSpec('P')
else:
    P = TypeVar('P')



class SlashCommandBot(Client):
    def __init__(
            self,
            *,
            loop: Optional[asyncio.AbstractEventLoop] = None,
            register_startup: bool = False,
            **options: Any):
        super().__init__(loop=loop, **options)
        self.register_startup = register_startup
        self.commands: dict[str, Command] = {}

    def slash_command(
            self,
            name: Optional[str] = None,
            *args: Any,
            **kwargs: Any,
    ):
        def decorator(func: Callable[[Concatenate[ContextT, P]], Coro[Any]] | Command):
            if not isinstance(func, Command):
                func = Command(func, name=name or func.__name__)

            self.commands[func.name] = func
            return func

        return decorator

    async def on_interaction(self, interaction: discord.Interaction) -> None:
        if not interaction.is_command():
            return
        name = interaction.data.get("name")
        command = self.commands.get(name, None)
        if command is None:
            return
        await command.handle(interaction, interaction.data.get("options", []))
