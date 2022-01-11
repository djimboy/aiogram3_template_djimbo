# - *- coding: utf- 8 - *-
import asyncio
import os
import sys

from aiogram import Bot, Dispatcher, Router, F

from tgbot.config import BOT_TOKEN, scheduler, get_admins
from tgbot.handlers.admin import setup_admin_handlers
from tgbot.handlers.user import setup_user_handlers
from tgbot.middlewares import setup_middlwares
from tgbot.services.api_session import RequestsSession
from tgbot.services.api_sqlite import create_bdx
from tgbot.utils.misc.bot_commands import set_commands
from tgbot.utils.misc.bot_logging import start_logging
from tgbot.utils.misc_functions import auto_backup, on_startup_notify


# Запуск шедулеров
async def scheduler_start(bot):
    scheduler.add_job(auto_backup, "interval", seconds=43200, args=(bot,))  # Автобэкап каждые 43200 секунд


async def main():
    create_bdx()

    scheduler.start()

    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    rSession = RequestsSession()

    # Создание роутеров
    admin_router = Router()
    user_router = Router()

    # Создание диспетчера и подключение роутеров
    dp = Dispatcher()
    dp.include_router(admin_router)
    dp.include_router(user_router)

    # Подключение мидлварей
    setup_middlwares(admin_router)
    setup_middlwares(user_router)

    # Подключение фильтров
    admin_router.message.filter(F.from_user.id.in_(get_admins()) & F.chat.type == "private")
    user_router.message.filter(F.chat.type == "private")

    # Подключение хендлеров
    setup_admin_handlers(admin_router)
    setup_user_handlers(user_router)

    try:
        await set_commands(bot)
        await on_startup_notify(bot)
        await scheduler_start(bot)

        print("~~~~~ Bot was started ~~~~~")
        logger.info("Bot was started")

        await bot.get_updates(offset=-1)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), rSession=rSession)
    finally:
        await rSession.close()
        await bot.session.close()


if __name__ == "__main__":
    logger = start_logging()

    try:
        # Исправление ошибки "RuntimeError: Event loop is closed" на Windows
        if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith("win"):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot was stopped")
    finally:
        if sys.platform.startswith("win"):
            os.system("cls")
        else:
            os.system("clear")
