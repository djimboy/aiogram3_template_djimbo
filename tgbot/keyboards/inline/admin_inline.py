# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.config import get_admins
from tgbot.utils.const_functions import ikb


# Кнопки главного меню
def menu_finl(user_id):
    keyboard = InlineKeyboardBuilder(
    ).row(
        ikb("User 1", data="open_user:1"), ikb("User 2", data="open_user:2")
    )

    if user_id in get_admins():
        keyboard.row(
            ikb("Admin 1", data="open_admin:1"), ikb("Admin 2", data="open_admin:2")
        )

    return keyboard.as_markup()
