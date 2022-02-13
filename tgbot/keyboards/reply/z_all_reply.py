# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.utils.const_functions import rkb

# Тестовые инлайн кнопки
test_rep = ReplyKeyboardBuilder(
).row(
    rkb("User 1"),
    rkb("User 2"),
).row(
    rkb("User 3"),
).as_markup(resize_keyboard=True)
