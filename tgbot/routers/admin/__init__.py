# - *- coding: utf- 8 - *-
from aiogram import Router

from tgbot.routers.admin.admin_menu import router_admin_menu


# Подключение хендлеров для админа
def setup_admin_handlers(admin_router: Router):
    admin_router.include_router(router_admin_menu)
