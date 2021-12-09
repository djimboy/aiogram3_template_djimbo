# - *- coding: utf- 8 - *-
from aiogram import BaseMiddleware, types

from tgbot.services.api_sqlite import get_userx, add_userx, delete_userx, update_userx
from tgbot.utils.free_functions import clear_html


class ExistsUserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: types.Message, data):
        get_user = event.from_user

        if not get_user.is_bot:
            user_id = get_user.id
            user_login = get_user.username
            user_name = clear_html(get_user.first_name)

            get_user_id = get_userx(user_id=user_id)

            if get_user_id is None:
                if user_login is not None:
                    get_user_login = get_userx(user_login=user_login)
                    if get_user_login is None:
                        add_userx(user_id, user_login.lower(), user_name)
                    else:
                        delete_userx(user_login=user_login)
                        add_userx(user_id, user_login.lower(), user_name)
                else:
                    add_userx(user_id, user_login, user_name)
            else:
                if user_name != get_user_id['user_name']:
                    update_userx(get_user_id['user_id'], user_name=user_name)
                if user_login is not None:
                    if user_login.lower() != get_user_id['user_login']:
                        update_userx(get_user_id['user_id'], user_login=user_login.lower())

        return await handler(event, data)
