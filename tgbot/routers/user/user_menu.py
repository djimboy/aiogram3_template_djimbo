# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.types import Message

from tgbot.keyboards.admin_inline import menu_finl
from tgbot.keyboards.z_all_inline import user_inl
from tgbot.keyboards.z_all_reply import user_rep
from tgbot.utils.misc.bot_models import UserDB, FSM, RS

router_user_menu = Router()


# Кнопка - User Inline
@router_user_menu.message(text="User Inline")
async def user_button_inline(message: Message, bot: Bot, state: FSM, rSession: RS, user: UserDB):
    await state.clear()

    await message.answer("Click Button - User Inline", reply_markup=user_inl)


# Кнопка - User Reply
@router_user_menu.message(text="User Reply")
async def user_button_reply(message: Message, bot: Bot, state: FSM, rSession: RS, user: UserDB):
    await state.clear()

    await message.answer("Click Button - User Reply", reply_markup=user_rep)


# Команда - /inline
@router_user_menu.message(commands="inline")
async def user_command_inline(message: Message, bot: Bot, state: FSM, rSession: RS, user: UserDB):
    await state.clear()

    await message.answer("Click command - /inline", reply_markup=menu_finl(message.from_user.id))
