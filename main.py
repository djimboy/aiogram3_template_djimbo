# - *- coding: utf- 8 - *-
import asyncio
import os
import sys

from aiogram import Bot, Dispatcher

from tgbot.config import BOT_TOKEN, scheduler
from tgbot.middlewares import register_all_middlwares
from tgbot.routers import register_all_routers
from tgbot.services.api_session import RequestsSession
from tgbot.services.api_sqlite import create_bdx
from tgbot.utils.misc.bot_commands import set_commands
from tgbot.utils.misc.bot_logging import start_logging
from tgbot.utils.misc_functions import autobackup, startup_notify


# Запуск шедулеров
async def scheduler_start(bot):
    scheduler.add_job(autobackup, "cron", hour=00, args=(bot,))  # Автобэкап в 12:00
    scheduler.add_job(autobackup, "cron", hour=12, args=(bot,))  # Автобэкап в 00:00


# Запуск бота и функций
async def main():
    create_bdx()

    scheduler.start()
    dispatcher = Dispatcher()
    rSession = RequestsSession()
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

    # Подключение хендлеров
    register_all_middlwares(dispatcher)  # Регистрация всех мидлварей
    register_all_routers(dispatcher)  # Регистрация всех роутеров

    try:
        await set_commands(bot)
        await startup_notify(bot)
        await scheduler_start(bot)

        print("~~~~~ Bot was started ~~~~~")
        logger.warning("Bot was started")

        await bot.get_updates(offset=-1)
        await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types(), rSession=rSession)
    finally:
        await rSession.close()
        await bot.session.close()


if __name__ == "__main__":
    logger = start_logging()

    try:
        # Исправление ошибки "RuntimeError: Event loop is closed" на Windows
        # if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith("win"):
        #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot was stopped")
    finally:
        if sys.platform.startswith("win"):
            os.system("cls")
        else:
            os.system("clear")
