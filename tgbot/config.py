# - *- coding: utf- 8 - *-
import configparser

from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

config = configparser.ConfigParser()
config.read("settings.ini")

BOT_TOKEN = config["settings"]["token"].strip()
PATH_DATABASE = "tgbot/data/database.db"  # Путь к БД
PATH_LOGS = "tgbot/data/logs.log"  # Путь к Логам


# Получение администраторов бота
def get_admins():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    admins = config["settings"]["admin_id"].strip()
    admins = admins.replace(" ", "")
    save_admins = []

    if "," in admins:
        admins = admins.split(",")
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []
            print("***** ENTER ADMIN ID IN SETTINGS.ini *****")

    if "" in admins:
        admins.remove("")
    if " " in admins:
        admins.remove(" ")

    for admin in admins:
        save_admins.append(int(admin))

    return save_admins
