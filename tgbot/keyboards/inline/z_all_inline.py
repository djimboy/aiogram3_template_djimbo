# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.utils.const_functions import ikb

# Test inline keyboard
test_inl = InlineKeyboardBuilder(
).row(
    ikb("Test 1", data="..."),
    ikb("Test 2", data="..."),
).row(
    ikb("Test 3", data="..."),
)
