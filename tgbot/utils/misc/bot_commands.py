# - *- coding: utf- 8 - *-
from aiogram import types, Bot
from aiogram.types import BotCommandScopeChat

from tgbot.config import get_admins

# Commands for users
default_commands = [
    types.BotCommand(command="start", description="♻ Restart the bot"),
]

# Commands for admins
admin_commands = [
    types.BotCommand(command="start", description="♻ Restart the bot"),
]


# Set commands
async def set_commands(bot: Bot):
    await bot.set_my_commands(default_commands)

    for admin in get_admins():
        await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin))