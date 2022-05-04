# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.utils.const_functions import ikb

# Тестовые инлайн кнопки
test_inl = InlineKeyboardBuilder(
).row(
    ikb("Test 1", data="..."),
    ikb("Test 2", data="..."),
).row(
    ikb("Test 3", data="..."),
).as_markup()
