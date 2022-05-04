# - *- coding: utf- 8 - *-
from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Update

from tgbot.utils.misc.bot_logging import start_logging

router_errors = Router()


# Обработка ошибок
@router_errors.errors()
async def errors_handler(update: Update, exception: TelegramAPIError):
    start_logging().exception(
        f"Exception: {str(exception)}\n"
        f"Update: {update.dict()}"
    )
