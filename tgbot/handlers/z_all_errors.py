# - *- coding: utf- 8 - *-
from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Update

from tgbot.utils.misc.bot_logging import start_logging

logger = start_logging()


# Обработка ошибок
async def errors_handler(update: Update, exception: TelegramAPIError):
    logger.exception(
        f"{str(exception)}.\n"
        f"Update: {update.dict()}"
    )


def register_all_errors(router: Router):
    router.errors.register(errors_handler)
