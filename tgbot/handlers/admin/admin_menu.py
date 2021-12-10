# - *- coding: utf- 8 - *-
from aiogram import types, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import FSInputFile

from tgbot.config import database_path
from tgbot.keyboards.inline import test_inl
from tgbot.utils.free_functions import get_date


# Button processing - Admin 1
async def admin_btn_one(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - Admin 1",
                         reply_markup=test_inl)


# Button processing - Admin 2
async def admin_btn_two(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - Admin 2",
                         reply_markup=test_inl)


# Button processing - Admin 3
async def admin_btn_three(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("Click Button - Admin 2",
                         reply_markup=test_inl)


# Get database
async def admin_database(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer_document(FSInputFile(database_path),
                                  caption=f"<b>📦 BACKUP</b>\n"
                                          f"<code>🕰 {get_date()}</code>")


def register_admin_menu(router: Router):
    router.message.register(admin_btn_one, text="Admin 1", state="*")
    router.message.register(admin_btn_two, text="Admin 2", state="*")
    router.message.register(admin_btn_three, text="Admin 3", state="*")

    router.message.register(admin_database, commands="getbd", state="*")
