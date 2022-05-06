# - *- coding: utf- 8 - *-
from aiogram import BaseMiddleware, types

from tgbot.services.api_sqlite import get_userx, add_userx, delete_userx, update_userx
from tgbot.utils.const_functions import clear_html
from tgbot.utils.misc.bot_models import WrapperMapDict


# Проверка юзеров в БД и их добавление
class ExistsUserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: types.Message, data):
        get_user = event.from_user

        if not get_user.is_bot:
            user_id = get_user.id
            user_login = get_user.username
            user_name = clear_html(get_user.first_name)
            user_surname = clear_html(get_user.last_name)

            if user_login is None: user_login = ""
            if user_surname is None: user_surname = ""

            get_user_id = get_userx(user_id=user_id)

            if get_user_id is None:
                if user_login is not None:
                    get_user_login = get_userx(user_login=user_login)
                    if get_user_login is None:
                        add_userx(user_id, user_login.lower(), user_name, user_surname)
                    else:
                        delete_userx(user_login=user_login)
                        add_userx(user_id, user_login.lower(), user_name, user_surname)
                else:
                    add_userx(user_id, user_login, user_name, user_surname)
            else:
                if user_name != get_user_id['user_name']:
                    update_userx(get_user_id['user_id'], user_name=user_name)
                if user_surname != get_user_id['user_surname']:
                    update_userx(get_user_id['user_id'], user_surname=user_surname)
                if user_login is not None:
                    if user_login.lower() != get_user_id['user_login']:
                        update_userx(get_user_id['user_id'], user_login=user_login.lower())
                else:
                    update_userx(get_user_id['user_id'], user_login="")

                data['user'] = WrapperMapDict(get_userx(user_id=user_id))

        return await handler(event, data)
