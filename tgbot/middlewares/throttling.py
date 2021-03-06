# - *- coding: utf- 8 - *-
import time
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.event.handler import HandlerObject
from aiogram.types import Message

from tgbot.services.api_sqlite import get_userx


# Антиспам
class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, default_rate: int = 0.6) -> None:
        self.default_rate = default_rate
        self.now_rate = default_rate

        self.last_throttled = int(time.time())
        self.count_throttled = 0

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data, ):
        real_handler: HandlerObject = data['handler']
        skip_pass = True

        this_user = data.get("event_from_user")
        if not this_user.is_bot:
            data['get_user'] = get_userx(user_id=this_user.id)

        if real_handler.flags.get("skip_pass") is not None:
            skip_pass = real_handler.flags.get("skip_pass")

        if skip_pass:
            if int(time.time()) - self.last_throttled >= self.now_rate:
                self.last_throttled = int(time.time())
                self.now_rate = self.default_rate
                self.count_throttled = 0

                return await handler(event, data)
            else:
                if self.count_throttled == 0:
                    self.count_throttled += 1
                    self.now_rate = self.default_rate * 2

                    return await handler(event, data)
                elif self.count_throttled == 1:
                    self.count_throttled += 1
                    self.now_rate = self.default_rate * 2

                    await event.reply("<b>❗ Пожалуйста, не спамьте.</b>")
                else:
                    self.now_rate = 3

                    if self.count_throttled == 2:
                        self.count_throttled = 3
                        await event.reply("<b>❗ Бот не будет отвечать до прекращения спама.</b>")

            self.last_throttled = int(time.time())
        else:
            return await handler(event, data)
