# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.utils.free_functions import ikb

test_inl = InlineKeyboardBuilder(
).row(
    ikb("Test 1", data="..."),
    ikb("Test 2", data="..."),
).row(
    ikb("Test 3", data="..."),
).as_markup()
