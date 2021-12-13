# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup

from tgbot.utils.free_functions import ikb

test_inl = InlineKeyboardMarkup(inline_keyboard=[
    [
        ikb("Test 1", data="..."),
        ikb("Test 2", data="..."),
    ],
    [
        ikb("Test 3", data="..."),
    ],
])
