# - *- coding: utf- 8 - *-
import time
from datetime import datetime

from aiogram.types import InlineKeyboardButton, KeyboardButton


# Clear HTML tags
def clear_html(get_text):
    if "<" in get_text: get_text = get_text.replace("<", "*")
    if ">" in get_text: get_text = get_text.replace(">", "*")

    return get_text


# Split list into several parts
def split_messages(get_list, count):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Build replay button
def rkb(text):
    return KeyboardButton(text=text)


# Build inline button
def ikb(text, data=None, url=None):
    if data is not None:
        return InlineKeyboardButton(text=text, callback_data=data)
    else:
        return InlineKeyboardButton(text=text, url=url)


# Get date
def get_date():
    dt = datetime.today().replace(microsecond=0)
    dt = dt.strftime("%d.%m.%Y %H:%M:%S")

    return dt


# Get unix date
def get_unix():
    return int(time.time()) + 10800


######################################## NUMBERS ########################################
# Converting a number to a real
def to_float(get_number):
    if "," in get_number:
        get_number = get_number.replace(",", ".")

    get_number = round(float(get_number), 2)

    if str(get_number).split(".")[1] == "0":
        get_number = int(get_number)

    return get_number


# Checking a number for a real
def is_float(get_number):
    try:
        if "," in get_number:
            get_number = get_number.replace(",", ".")
        float(get_number)

        return False
    except ValueError:
        return True


# Converting a number to an integer
def to_int(get_number):
    if "," in get_number:
        get_number = get_number.replace(",", ".")

    get_number = int(round(float(get_number)))

    return get_number


# Checking a number for an integer
def is_int(get_number):
    if get_number.isdigit():
        return True
    else:
        return False
