# - *- coding: utf- 8 - *-
from aiogram import types, Router, Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import FSInputFile

from tgbot.config import PATH_DATABASE, PATH_LOGS
from tgbot.keyboards.z_all_inline import test_inl
from tgbot.keyboards.z_all_reply import test_rep
from tgbot.utils.const_functions import get_date

router_admin_menu = Router()


# Кнопка - Admin Inline
@router_admin_menu.message(text="Admin Inline")
async def admin_button_inline(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - Admin Inline", reply_markup=test_inl)


# Кнопка - Admin Reply
@router_admin_menu.message(text="Admin Reply")
async def admin_button_reply(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - Admin Reply", reply_markup=test_rep)


# Получение Базы Данных
@router_admin_menu.message(commands=['db', 'database'])
async def admin_database(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer_document(FSInputFile(PATH_DATABASE),
                                  caption=f"<b>📦 BACKUP</b>\n"
                                          f"<code>🕰 {get_date()}</code>")


# Получение логов
@router_admin_menu.message(commands=['log', 'logs'])
async def admin_log(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer_document(FSInputFile(PATH_LOGS),
                                  caption=f"<code>🕰 {get_date()}</code>")
