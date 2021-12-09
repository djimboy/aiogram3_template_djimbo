# - *- coding: utf- 8 - *-
from aiogram import Router

from tgbot.filters import setup_filters
from tgbot.handlers import setup_handlers
from tgbot.middlewares import setup_middlwares


def setup_events(router: Router):
    setup_middlwares(router)
    setup_filters(router)
    setup_handlers(router)
