# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.config import get_admins
from tgbot.utils.const_functions import rkb


# Кнопки главного меню
def menu_frep(user_id):
    keyboard = ReplyKeyboardBuilder(
    ).row(
        rkb("User 1"), rkb("User 2"), rkb("User 3")
    )

    if user_id in get_admins():
        keyboard.row(
            rkb("Admin 1"), rkb("Admin 2"), rkb("Admin 3")
        )

    return keyboard.as_markup(resize_keyboard=True)
