# - *- coding: utf- 8 - *-
from aiogram import types, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.admin_reply import menu_frep

router_missed = Router()


# Колбэк с удалением сообщения
@router_missed.callback_query(text="close_this")
async def processing_callback_remove(call: CallbackQuery, state: FSMContext):
    await call.message.delete()


# Колбэк с обработкой кнопки
@router_missed.callback_query(text="...")
async def processing_callback_answer(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=20)


# Колбэк с обработкой удаления сообщений потерявших стейт
@router_missed.callback_query()
async def processing_callback_missed(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except:
        pass

    await call.message.answer("<b>❌ Данные не были найдены из-за перезапуска скрипта.\n"
                              "♻ Выполните действие заново.</b>",
                              reply_markup=menu_frep(call.from_user.id))


# Обработка всех неизвестных команд
@router_missed.message()
async def processing_message_missed(message: types.Message):
    await message.answer("♦ Неизвестная команда.\n"
                         "▶ Введите /start")
