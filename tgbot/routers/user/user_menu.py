# - *- coding: utf- 8 - *-
from aiogram import types, Router, Bot
from aiogram.dispatcher.fsm.context import FSMContext

from tgbot.keyboards.admin_inline import menu_finl
from tgbot.keyboards.z_all_inline import test_inl
from tgbot.keyboards.z_all_reply import test_rep

router_user_menu = Router()


# Кнопка - User Inline
@router_user_menu.message(text="User Inline")
async def user_button_inline(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - User Inline", reply_markup=test_inl)


# Кнопка - User Reply
@router_user_menu.message(text="User Reply")
async def user_button_reply(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - User Reply", reply_markup=test_rep)


# Команда - /inline
@router_user_menu.message(commands="inline")
async def user_command_inline(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click command - /inline", reply_markup=menu_finl(message.from_user.id))
