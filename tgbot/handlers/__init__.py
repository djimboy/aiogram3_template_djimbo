# - *- coding: utf- 8 - *-
from aiogram import Router

from tgbot.handlers.admin_menu import register_admin_menu
from tgbot.handlers.main_start import register_main_start
from tgbot.handlers.z_all_errors import register_all_errors
from tgbot.handlers.z_all_missed import register_all_missed


def setup_handlers(router: Router):
    register_all_errors(router)
    register_main_start(router)
    register_admin_menu(router)
    register_all_missed(router)
