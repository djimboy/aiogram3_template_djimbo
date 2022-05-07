# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.types import FSInputFile, Message

from tgbot.config import PATH_DATABASE, PATH_LOGS
from tgbot.keyboards.z_all_inline import admin_inl
from tgbot.keyboards.z_all_reply import admin_rep
from tgbot.utils.misc.bot_models import UserDB, FSM, RS
from tgbot.utils.const_functions import get_date

router_admin_menu = Router()


# Кнопка - Admin Inline
@router_admin_menu.message(text="Admin Inline")
async def admin_button_inline(message: Message, bot: Bot, state: FSM, rSession: RS, user: UserDB):
    await state.clear()

    await message.answer("Click Button - Admin Inline", reply_markup=admin_inl)


# Кнопка - Admin Reply
@router_admin_menu.message(text="Admin Reply")
async def admin_button_reply(message: Message, bot: Bot, state: FSM, rSession: RS, user: UserDB):
    await state.clear()

    await message.answer("Click Button - Admin Reply", reply_markup=admin_rep)


# Получение Базы Данных
@router_admin_menu.message(commands=['db', 'database'])
async def admin_database(message: Message, bot: Bot, state: FSM, rSession: RS, user: UserDB):
    await state.clear()

    await message.answer_document(FSInputFile(PATH_DATABASE),
                                  caption=f"<b>📦 BACKUP</b>\n"
                                          f"<code>🕰 {get_date()}</code>")


# Получение логов
@router_admin_menu.message(commands=['log', 'logs'])
async def admin_log(message: Message, bot: Bot, state: FSM, rSession: RS, user: UserDB):
    await state.clear()

    await message.answer_document(FSInputFile(PATH_LOGS), caption=f"<code>🕰 {get_date()}</code>")
