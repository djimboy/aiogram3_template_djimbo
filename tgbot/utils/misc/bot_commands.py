# - *- coding: utf- 8 - *-
from aiogram import types, Bot
from aiogram.types import BotCommandScopeChat

from tgbot.config import get_admins

# Commands for users
default_commands = [
    types.BotCommand(command="start", description="♻ Перезапустить бота"),
]

# Commands for admins
admin_commands = [
    types.BotCommand(command="start", description="♻ Перезапустить бота"),
]


# Set commands
async def set_commands(bot: Bot):
    await bot.set_my_commands(default_commands)

    for admin in get_admins():
        try:
            await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin))
        except:
            pass
