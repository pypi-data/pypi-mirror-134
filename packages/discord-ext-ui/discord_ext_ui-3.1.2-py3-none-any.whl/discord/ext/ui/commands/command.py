from __future__ import annotations

from typing import Callable, TYPE_CHECKING, TypeVar, Any, Optional

import discord
from discord.types.interactions import ApplicationCommandInteractionDataOption
from typing_extensions import Concatenate, ParamSpec

from .context import ContextT, Context
from .types import Coro, CommandOptionType

if TYPE_CHECKING:
    P = ParamSpec('P')
    from .bot import SlashCommandBot
else:
    P = TypeVar('P')


class _MISSING:
    def __eq__(self, other):
        return isinstance(other, _MISSING)


MISSING = _MISSING()


class Command:
    def __init__(self, func: Callable[[Concatenate[ContextT, P]], Coro[Any]], *, name: str):
        self.func = func
        self.name = name
        self.options: dict[str, Option] = {}

        for op in getattr(func, "__command_options__", []):  # type: Option
            self.add_option(op)

        self.bot: "SlashCommandBot" | None = None

    def add_option(self, op: Option):
        self.options[op.display_name] = op

    def get_option_mapping(self) -> dict:
        return {op.display_name: op.name for op in self.options.values()}

    async def handle(self, interaction: discord.Interaction, options: list[ApplicationCommandInteractionDataOption]):
        key_mapping = self.get_option_mapping()
        mapping: dict[str, Any] = {}

        for option in options:
            name = option["name"]
            option_type = option["type"]
            value = option["value"]
            converted_value = value

            if option_type == 6:
                converted_value = self.bot.get_user(value)
            elif option_type == 7:
                converted_value = self.bot.get_channel(value)
            elif option_type == 8:
                converted_value = interaction.guild.get_role(value)
            elif option_type == 9:
                converted_value = self.bot.get_user(value)
                if converted_value is None:
                    converted_value = interaction.guild.get_role(value)

            mapping[key_mapping[name]] = converted_value

        ctx = Context(interaction, state=self.bot)
        await self.func(ctx, **mapping)


class Option:
    def __init__(self, name: str, description: str, option_type: CommandOptionType, *, display_name: Optional[str] = None):
        self.name = name
        self.description = description
        self.type = option_type
        self.required = False
        self.display_name = display_name or self.name


def option(name: str, description: str, option_type: CommandOptionType, *, display_name: Optional[str] = None):
    def decorator(func: Callable[[Concatenate[ContextT, P]], Coro[Any]]):

        options = getattr(func, "__command_options__", [])
        options.append(Option(name, description, option_type, display_name=display_name))
        func.__command_options__ = options
        return func

    return decorator
