# - *- coding: utf- 8 - *-
import random
import time
from datetime import datetime

from aiogram.types import InlineKeyboardButton, KeyboardButton


# Очистка HTML тэгов
def clear_html(get_text: str):
    if get_text is not None:
        if "<" in get_text: get_text = get_text.replace("<", "*")
        if ">" in get_text: get_text = get_text.replace(">", "*")

    return get_text


# Очистка пробелов в списке
def clear_list(get_list: list):
    if "" in get_list:
        get_list.remove("")

    if " " in get_list:
        get_list.remove(" ")

    return get_list


# Разбив списка на несколько частей
def split_messages(get_list: list, count: int):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Генерация реплай кнопки
def rkb(text):
    return KeyboardButton(text=text)


# Генерация инлайн кнопки
def ikb(text, data=None, url=None):
    if data is not None:
        return InlineKeyboardButton(text=text, callback_data=data)
    else:
        return InlineKeyboardButton(text=text, url=url)


# Получение даты
def get_date():
    dt = datetime.today().replace(microsecond=0)
    dt = dt.strftime("%d.%m.%Y %H:%M:%S")

    return dt


# Получение юникс даты
def get_unix():
    return int(time.time()) + 10800


# Генерация пароля
def generate_password(len_password: int):
    passwd = list("1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
    random.shuffle(passwd)
    random_chars = "".join([random.choice(passwd) for x in range(len_password)])

    return random_chars


# Корректный вывод слов - День
def convert_day(day):
    day = int(day)
    days = ["день", "дня", "дней"]

    if day % 10 == 1 and day % 100 != 11:
        count = 0
    elif 2 <= day % 10 <= 4 and (day % 100 < 10 or day % 100 >= 20):
        count = 1
    else:
        count = 2

    return f"{day} {days[count]}"


# Форматирование числа в читаемый вид
def format_rate(rate, around=False):
    rate = str(round(float(rate), 2))

    if "," in rate:
        rate = float(rate.replace(",", "."))

    len_rate = str(int(float(rate)))

    if len(len_rate) == 3:
        get_rate = str(len_rate)
    elif len(len_rate) == 4:
        get_rate = f"{len_rate[0]} {len_rate[1:]}"
    elif len(len_rate) == 5:
        get_rate = f"{len_rate[0:2]} {len_rate[2:]}"
    elif len(len_rate) == 6:
        get_rate = f"{len_rate[0:3]} {len_rate[3:]}"
    elif len(len_rate) == 7:
        get_rate = f"{len_rate[0:1]} {len_rate[1:4]} {len_rate[4:]}"
    elif len(len_rate) == 8:
        get_rate = f"{len_rate[0:2]} {len_rate[2:5]} {len_rate[5:]}"
    elif len(len_rate) == 9:
        get_rate = f"{len_rate[0:3]} {len_rate[3:6]} {len_rate[6:]}"
    elif len(len_rate) == 10:
        get_rate = f"{len_rate[0:1]} {len_rate[1:4]} {len_rate[4:7]} {len_rate[7:]}"

    if not around:
        if "." in rate:
            dot_amount = rate.find(".")
            get_rate += f"{rate[dot_amount:]}"

    return get_rate


######################################## ЧИСЛА ########################################
# Конвертация числа в вещественное
def to_float(get_number):
    if "," in get_number:
        get_number = get_number.replace(",", ".")

    get_number = round(float(get_number), 2)

    if str(get_number).split(".")[1] == "0":
        get_number = int(get_number)

    return get_number


# Проверка числа на вещественное
def is_float(get_number):
    try:
        if "," in get_number:
            get_number = get_number.replace(",", ".")
        float(get_number)

        return True
    except ValueError:
        return False


# Конвертация числа в целочисленное
def to_int(get_number):
    if "," in get_number:
        get_number = get_number.replace(",", ".")

    get_number = int(round(float(get_number)))

    return get_number


# Проверка числа на целочисленное
def is_int(get_number):
    if get_number.isdigit():
        return True
    else:
        return False


# Преобразование длинных вещественных чисел в читаемый вид
def show_floats(amount):
    return f"{float(amount):.8f}"
