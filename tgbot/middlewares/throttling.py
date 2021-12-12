# - *- coding: utf- 8 - *-
import time

from aiogram import BaseMiddleware, types


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, default_rate: int = 0.5) -> None:
        self.default_rate = default_rate
        self.count_throttled = 1
        self.last_throttled = 0

    async def __call__(self, handler, event: types.Message, data):
        if int(time.time()) - self.last_throttled >= self.default_rate:
            self.last_throttled = int(time.time())
            self.default_rate = 0.5
            self.count_throttled = 0
            return await handler(event, data)
        else:
            if self.count_throttled >= 2:
                self.default_rate = 3
            else:
                self.count_throttled += 1
                await event.reply("<b>❗ Пожалуйста, не спамьте.</b>")

        self.last_throttled = int(time.time())
