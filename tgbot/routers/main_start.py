# - *- coding: utf- 8 - *-
from aiogram import Router
from aiogram import types
from aiogram.dispatcher.fsm.context import FSMContext

from tgbot.keyboards.admin_reply import menu_frep

router_start = Router()


# Открытие главного меню
@router_start.message(text_startswith=["⬅ Главное меню", "/start"])
async def main_start(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("🔸 Бот готов к использованию.\n"
                         "🔸 Если не появились вспомогательные кнопки\n"
                         "▶ Введите /start",
                         reply_markup=menu_frep(message.from_user.id))
