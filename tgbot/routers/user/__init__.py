# - *- coding: utf- 8 - *-
from aiogram import Router

from tgbot.routers.user.user_menu import router_user_menu


# Подключение хендлеров для юзера
def setup_user_handlers(user_router: Router):
    user_router.include_router(router_user_menu)
