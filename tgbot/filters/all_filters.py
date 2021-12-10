# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher.filters import BaseFilter


# Test filter
class IsTest(BaseFilter):
    async def __call__(self, message: types.Message):
        if "test" in ["test"]:
            return True
        else:
            return False
