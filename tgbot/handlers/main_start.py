# - *- coding: utf- 8 - *-
from aiogram import Router
from aiogram import types
from aiogram.dispatcher.fsm.context import FSMContext

from tgbot.filters import IsPrivate
from tgbot.keyboards.reply import menu_frep


# Processing commands - /start
async def main_start(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("<b>🔸 The bot is ready to use.</b>\n"
                         "🔸 If the buttons are not displayed\n"
                         "▶ Enter /start",
                         reply_markup=menu_frep(message.from_user.id))


def register_main_start(router: Router):
    router.message.register(main_start, commands=["start"], state="*")
