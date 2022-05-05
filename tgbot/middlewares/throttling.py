# - *- coding: utf- 8 - *-
import time

from aiogram import BaseMiddleware, types
from aiogram.dispatcher.event.handler import HandlerObject


# Антиспам
class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, default_rate: int = 1) -> None:
        self.last_throttled = int(time.time())
        self.default_rate = default_rate
        self.now_rate = default_rate
        self.count_throttled = 0

    async def __call__(self, handler, event: types.Message, data):
        real_handler: HandlerObject = data["handler"]
        skip_pass = True

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
                    self.now_rate = self.default_rate * 1.5

                    return await handler(event, data)
                elif self.count_throttled == 1:
                    self.count_throttled += 1
                    self.now_rate = self.default_rate * 2
                    await event.reply("<b>❗ Пожалуйста, не спамьте.</b>")
                else:
                    self.now_rate = 3

            self.last_throttled = int(time.time())
        else:
            return await handler(event, data)
