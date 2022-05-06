# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.keyboards.admin_reply import menu_frep
from tgbot.services.api_session import RequestsSession as RS
from tgbot.utils.misc.bot_models import UserDB

router_start = Router()


# Открытие главного меню
@router_start.message(text_startswith=["⬅ Главное меню", "/start"])
async def main_starte(message: Message, bot: Bot, state: FSMContext, rSession: RS, user: UserDB):
    await state.clear()

    await message.answer("🔸 Бот готов к использованию.\n"
                         "🔸 Если не появились вспомогательные кнопки\n"
                         "▶ Введите /start",
                         reply_markup=menu_frep(message.from_user.id))
