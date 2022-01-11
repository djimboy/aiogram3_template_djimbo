# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.utils.const_functions import rkb

# Test reply keyboard
test_rep = ReplyKeyboardBuilder(
).row(
    rkb("Test 1"),
    rkb("Test 2"),
).row(
    rkb("Test 3"),
)
