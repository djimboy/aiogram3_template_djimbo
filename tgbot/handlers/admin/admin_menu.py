# - *- coding: utf- 8 - *-
from aiogram import types, Router, Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import FSInputFile

from tgbot.config import DATABASE_PATH
from tgbot.keyboards.inline import test_inl
from tgbot.keyboards.reply import test_rep
from tgbot.utils.const_functions import get_date


# Button - Admin Inline
async def admin_button_inline(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - Admin Inline", reply_markup=test_inl)


# Button - Admin Reply
async def admin_button_reply(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - Admin Reply", reply_markup=test_rep)


# Get Database
async def admin_database(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer_document(FSInputFile(DATABASE_PATH),
                                  caption=f"<b>📦 BACKUP</b>\n"
                                          f"<code>🕰 {get_date()}</code>")


# Get logs
async def admin_log(message: types.Message, bot: Bot, rSession, state: FSMContext):
    await state.clear()

    await message.answer_document(FSInputFile("logs.log"),
                                  caption=f"<code>🕰 {get_date()}</code>")


def register_admin_menu(router: Router):
    router.message.register(admin_button_inline, text="Admin Inline", state="*")
    router.message.register(admin_button_reply, text="Admin Reply", state="*")

    router.message.register(admin_database, commands="db", state="*")
    router.message.register(admin_log, commands="log", state="*")
