# - *- coding: utf- 8 - *-
from aiogram import Router
from aiogram import types
from aiogram.dispatcher.fsm.context import FSMContext

from tgbot.keyboards.reply import menu_frep


# Processing commands - /start
async def main_start(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("<b>🔸 Бот готов к использованию.</b>\n"
                         "🔸 Если не появились вспомогательные кнопки\n"
                         "▶ Введите /start",
                         reply_markup=menu_frep(message.from_user.id))


def register_main_start(router: Router):
    router.message.register(main_start, commands=["start"], state="*")
