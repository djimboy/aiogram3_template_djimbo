# - *- coding: utf- 8 - *-
from aiogram import Dispatcher

from tgbot.middlewares.exists_user import ExistsUserMiddleware
from tgbot.middlewares.throttling import ThrottlingMiddleware


# Setup middlawares
def setup_middlwares(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())
    dp.message.outer_middleware(ExistsUserMiddleware())
    dp.callback_query.outer_middleware(ExistsUserMiddleware())
