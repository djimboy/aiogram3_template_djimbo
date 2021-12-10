# - *- coding: utf- 8 - *-
from aiogram import types, Router
from aiogram.dispatcher.fsm.context import FSMContext

from tgbot.keyboards.inline import test_inl


# Button processing - User 1
async def user_btn_one(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - User 1",
                         reply_markup=test_inl)


# Button processing - User 2
async def user_btn_two(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - User 2",
                         reply_markup=test_inl)


# Button processing - User 3
async def user_btn_three(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - User 3",
                         reply_markup=test_inl)


def register_user_menu(router: Router):
    router.message.register(user_btn_one, text="User 1", state="*")
    router.message.register(user_btn_two, text="User 2", state="*")
    router.message.register(user_btn_three, text="User 3", state="*")
