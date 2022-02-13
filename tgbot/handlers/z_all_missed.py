# - *- coding: utf- 8 - *-
from aiogram import types, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.reply import menu_frep


# Processing callback the message deletion
async def processing_callback_remove(call: CallbackQuery, state: FSMContext):
    await call.message.delete()


# Processing callback the inline button processing
async def processing_callback_answer(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)


# Processing all callbacks with empty state
async def processing_callback_missed(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except:
        pass

    await call.message.answer("<b>❌ Data was not found due to script restart.\n"
                              "♻ Perform the action again.</b>",
                              reply_markup=menu_frep(call.from_user.id))


# Processing all unknown messages
async def processing_message_missed(message: types.Message):
    await message.answer("<b>♦ Unknown command.</b>\n"
                         "▶ Enter /start")


def register_all_missed(router: Router):
    router.callback_query.register(processing_callback_remove, text="close_this", state="*")
    router.callback_query.register(processing_callback_answer, text="...", state="*")
    router.callback_query.register(processing_callback_missed, state="*")

    router.message.register(processing_message_missed, state="*")
