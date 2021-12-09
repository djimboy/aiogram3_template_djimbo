# - *- coding: utf- 8 - *-
from aiogram import Bot
from aiogram.types import FSInputFile

from tgbot.config import get_admins, database_path
from tgbot.utils.free_functions import get_date


# Action after launching the bot (sending a message to all admins that the bot is running)
async def on_startup_notify(bot: Bot):
    if len(get_admins()) >= 1:
        await send_all_admin(bot, "<b>✅ Bot was started</b>")


# Automatic backups
async def auto_backup(bot: Bot):
    document = FSInputFile(database_path)

    for admin in get_admins():
        await bot.send_document(admin,
                                document,
                                caption=f"<b>📦 AUTOBACKUP</b>\n"
                                        f"<code>🕰 {get_date()}</code>")


# Sending a message to all admins
async def send_all_admin(bot: Bot, message, markup=None, not_me=0):
    for admin in get_admins():
        try:
            if str(admin) != str(not_me):
                await bot.send_message(admin, message, reply_markup=markup, disable_web_page_preview=True)
        except:
            pass
