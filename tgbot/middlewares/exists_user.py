# - *- coding: utf- 8 - *-
from aiogram import BaseMiddleware, types

from tgbot.services.api_sqlite import get_userx, add_userx, update_userx
from tgbot.utils.const_functions import clear_html
from tgbot.utils.misc.bot_models import WrapperMapDict


# Проверка юзеров в БД и их добавление
class ExistsUserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: types.Message, data):
        this_user = event.from_user

        if not this_user.is_bot:
            user_id = this_user.id
            user_login = this_user.username
            user_name = clear_html(this_user.first_name)
            user_surname = clear_html(this_user.last_name)

            if user_login is None: user_login = ""
            if user_surname is None: user_surname = ""

            get_user = get_userx(user_id=user_id)

            if get_user is None:
                add_userx(user_id, user_login.lower(), user_name, user_surname)
            else:
                if user_name != get_user['user_name']:
                    update_userx(get_user['user_id'], user_name=user_name)

                if user_surname != get_user['user_surname']:
                    update_userx(get_user['user_id'], user_surname=user_surname)

                if user_login.lower() != get_user['user_login']:
                    update_userx(get_user['user_id'], user_login=user_login.lower())

        data['user'] = WrapperMapDict(get_userx(user_id=user_id))

        return await handler(event, data)
