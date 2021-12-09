# - *- coding: utf- 8 - *-
from aiogram import Router

from tgbot.filters.all_filters import IsPrivate


def setup_filters(router: Router):
    router.message.filter(IsPrivate())
