# - *- coding: utf- 8 - *-
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault

from tgbot.config import get_admins

# Commands for users
user_commands = [
    BotCommand(command="start", description="♻ Restart bot"),
    BotCommand(command="inline", description="🌀 Get Inline Keyboard"),
]

# Commands for admins
admin_commands = [
    BotCommand(command="start", description="♻ Restart bot"),
    BotCommand(command="inline", description="🌀 Get Inline Keyboard"),
]


# Set commands
async def set_commands(bot: Bot):
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    for admin in get_admins():
        try:
            await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin))
        except:
            pass
