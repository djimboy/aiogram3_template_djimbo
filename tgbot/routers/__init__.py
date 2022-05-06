# - *- coding: utf- 8 - *-
from aiogram import Dispatcher, Router, F

from tgbot.config import get_admins
from tgbot.routers.admin import setup_admin_handlers
from tgbot.routers.main_start import router_start
from tgbot.routers.user import setup_user_handlers
from tgbot.routers.z_all_errors import router_errors
from tgbot.routers.z_all_missed import router_missed


# Подключение всех роутеров
def register_all_routers(dp: Dispatcher):
    # Создание образов роутера
    user_router = Router()
    admin_router = Router()

    # Инициализация роутеров
    dp.include_router(router_errors)
    dp.include_router(router_start)

    # Подключение фильтров
    admin_router.callback_query.filter(F.from_user.id.in_(get_admins()) & F.chat.type == "private")
    admin_router.message.filter(F.from_user.id.in_(get_admins()) & F.chat.type == "private")
    user_router.callback_query.filter(F.chat.type == "private")
    user_router.message.filter(F.chat.type == "private")

    # Подгрузка хендлеров в роутеры
    setup_user_handlers(user_router)
    setup_admin_handlers(admin_router)

    # Роутер с пропущенными хендлерами
    dp.include_router(user_router)
    dp.include_router(admin_router)
    dp.include_router(router_missed)
