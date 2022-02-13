# - *- coding: utf- 8 - *-
from aiogram import types, Router, Bot
from aiogram.dispatcher.fsm.context import FSMContext

from tgbot.keyboards.inline import test_inl
from tgbot.keyboards.inline.admin_inline import menu_finl
from tgbot.keyboards.reply import test_rep


# Button - User Inline
async def user_button_inline(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - User Inline", reply_markup=test_inl)


# Button - User Reply
async def user_button_reply(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - User Reply", reply_markup=test_rep)


# Command - /inline
async def user_command_inline(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click command - /inline", reply_markup=menu_finl(message.from_user.id))


def register_user_menu(router: Router):
    router.message.register(user_button_inline, text="User Inline", state="*")
    router.message.register(user_button_reply, text="User Reply", state="*")

    router.message.register(user_command_inline, commands="inline", state="*")
