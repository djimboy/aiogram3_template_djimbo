# - *- coding: utf- 8 - *-
import time
from typing import Optional

from aiogram import BaseMiddleware, types
from aiogram.types import User


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, default_rate: int = 0.5) -> None:
        self.default_rate = default_rate
        self.count_throttled = 1
        self.last_throttled = 0

    async def __call__(self, handler, event: types.Message, data):
        user: Optional[User] = data.get("event_from_user")

        if user:
            if int(time.time()) - self.last_throttled > self.default_rate:
                self.last_throttled = int(time.time())
                self.default_rate = 0.5
                self.count_throttled = 0
                return await handler(event, data)
            else:
                if self.count_throttled >= 2:
                    self.default_rate = 3
                else:
                    self.count_throttled += 1
                    await event.reply("<b>❗ Please, do not spam.</b>")

            self.last_throttled = int(time.time())
        else:
            return await handler(event, data)
