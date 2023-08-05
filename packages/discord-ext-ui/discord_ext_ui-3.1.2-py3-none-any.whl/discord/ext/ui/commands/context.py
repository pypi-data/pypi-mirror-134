from __future__ import annotations

from typing import TypeVar, TYPE_CHECKING, Optional

import discord

if TYPE_CHECKING:
    from .bot import SlashCommandBot
    from discord.interactions import InteractionChannel

ContextT = TypeVar('ContextT', bound='Context')


class Context:
    def __init__(self, interaction: discord.Interaction, *, state: "SlashCommandBot"):
        self.interaction: discord.Interaction = interaction
        self.response: discord.InteractionResponse = interaction.response
        self._state = state

        self.send_message = self.response.send_message

    @property
    def guild(self) -> Optional[discord.Guild]:
        return self.interaction.guild

    @property
    def channel(self) -> Optional[InteractionChannel]:
        return self.interaction.channel

    @property
    def message(self) -> Optional[discord.Message]:
        return self.interaction.message

    async def defer(self, ephemeral: bool = False) -> None:
        await self.response.defer(ephemeral=ephemeral)
