# - *- coding: utf- 8 - *-
from aiogram import Router

from tgbot.handlers.main_start import register_main_start
from tgbot.handlers.user.user_menu import register_user_menu
from tgbot.handlers.z_all_errors import register_all_errors
from tgbot.handlers.z_all_missed import register_all_missed


# Setup user handlers
def setup_user_handlers(router: Router):
    register_all_errors(router)
    register_main_start(router)
    register_user_menu(router)
    register_all_missed(router)
