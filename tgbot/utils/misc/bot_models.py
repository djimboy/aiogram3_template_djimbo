# - *- coding: utf- 8 - *-
from dataclasses import dataclass
from datetime import datetime


# Упрощённый вызов из словаря
class WrapperMapDict:
    def __init__(self, get_dict: dict):
        self.get_dict = get_dict

    def get_value(self):
        return self.get_dict

    def __getattr__(self, item: str) -> 'WrapperMapDict':
        return self.__class__(self.get_dict.get(item))

    def __repr__(self):
        return repr(self.get_dict)


# Модель пользователя
@dataclass
class UserDB:
    user_id: int
    user_login: str
    user_name: str
    user_surname: str
    user_date: datetime
    user_unix: int
