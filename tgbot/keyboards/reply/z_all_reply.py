# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.config import get_admins
from tgbot.utils.free_functions import rkb


# Main menu buttons
def menu_frep(user_id):
    keyboard = ReplyKeyboardBuilder(
    ).row(
        rkb("Test 1"), rkb("Test 2"), rkb("Test 3")
    )

    if str(user_id) in get_admins():
        keyboard.row(rkb("Admin 1"), rkb("Admin 2"))

    return keyboard.as_markup(resize_keyboard=True)
