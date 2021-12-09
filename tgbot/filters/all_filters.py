# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher.filters import BaseFilter

from tgbot.config import get_admins


# Checking for writing a message to a PM bot
class IsPrivate(BaseFilter):
    async def __call__(self, message: types.Message):
        return message.chat.type == "private"


# Checking for admin
class IsAdmin(BaseFilter):
    async def __call__(self, message: types.Message):
        if str(message.from_user.id) in get_admins():
            return True
        else:
            return False