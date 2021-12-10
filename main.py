# - *- coding: utf- 8 - *-
import asyncio
import os
import platform

from aiogram import Bot, Dispatcher, Router

from tgbot import setup_middlwares
from tgbot.config import BOT_TOKEN, scheduler
from tgbot.filters import IsPrivate
from tgbot.handlers.admin import setup_admin_handlers
from tgbot.handlers.user import setup_user_handlers
from tgbot.services.api_sqlite import create_bdx
from tgbot.utils.misc.bot_commands import set_commands
from tgbot.utils.misc.bot_logging import start_logging
from tgbot.utils.misc_functions import auto_backup, on_startup_notify


# Start sheduler functions
async def scheduler_default(bot):
    scheduler.add_job(auto_backup, "interval", seconds=43200, args=(bot,))  # Autobackup every 43200 seconds


async def main():
    create_bdx()

    scheduler.start()

    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    admin_router = Router()
    user_router = Router()
    dp = Dispatcher()

    setup_middlwares(admin_router)
    setup_middlwares(user_router)

    admin_router.message.filter(IsPrivate())
    user_router.message.filter(IsPrivate())

    setup_admin_handlers(admin_router)
    setup_user_handlers(user_router)

    dp.include_router(admin_router)
    dp.include_router(user_router)

    try:
        await set_commands(bot)
        await on_startup_notify(bot)
        await scheduler_default(bot)

        print("~~~~~ Bot was started ~~~~~")
        logger.info("Bot was started")

        await bot.get_updates(offset=-1)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logger = start_logging()

    try:
        asyncio.get_event_loop().run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot was stopped")
    finally:
        if platform.system().lower() == "windows":
            os.system("cls")
        else:
            os.system("clear")
