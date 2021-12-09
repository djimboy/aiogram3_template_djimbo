# - *- coding: utf- 8 - *-
from aiogram import Router

from tgbot.middlewares.exists_user import ExistsUserMiddleware
from tgbot.middlewares.throttling import ThrottlingMiddleware


def setup_middlwares(router: Router):
    router.message.outer_middleware(ThrottlingMiddleware())
    router.message.outer_middleware(ExistsUserMiddleware())
