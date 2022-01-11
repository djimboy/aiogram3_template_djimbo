# - *- coding: utf- 8 - *-
from aiogram import types, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.reply import menu_frep


# Колбэк с удалением сообщения
async def processing_callback_remove(call: CallbackQuery, state: FSMContext):
    await call.message.delete()


# Колбэк с обработкой кнопки
async def processing_callback_answer(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)


# Колбэк с обработкой удаления сообщений потерявших стейт
async def processing_callback_missed(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except:
        pass

    await call.message.answer("<b>❌ Данные не были найдены из-за перезапуска скрипта.\n"
                              "♻ Выполните действие заново.</b>",
                              reply_markup=menu_frep(call.from_user.id))


# Обработка всех неизвестных команд
async def processing_message_missed(message: types.Message):
    await message.answer("<b>♦ Неизвестная команда.</b>\n"
                         "▶ Введите /start")


def register_all_missed(router: Router):
    router.callback_query.register(processing_callback_remove, text="close_this", state="*")
    router.callback_query.register(processing_callback_answer, text="...", state="*")
    router.callback_query.register(processing_callback_missed, state="*")

    router.message.register(processing_message_missed, state="*")
