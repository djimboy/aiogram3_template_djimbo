# - *- coding: utf- 8 - *-
import sqlite3

from tgbot.config import database_path
from tgbot.utils.const_functions import get_unix, get_date


def dict_factory(cursor, row):
    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


# con.row_factory = sqlite3.Row

####################################################################################################
##################################### ФОРМАТИРОВАНИЕ ЗАПРОСОВ ######################################
# Форматирование запросов с аргументами
def update_format_with_args(sql, parameters: dict):
    if "XXX" not in sql:
        sql += " XXX "

    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)

    return sql, list(parameters.values())


# Форматирование запросов без аргументов
def get_format_args(sql, parameters: dict):
    sql = f"{sql} WHERE "

    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])

    return sql, list(parameters.values())


####################################### ЗАПРОСЫ К БАЗЕ ДАННЫХ ######################################
####################################################################################################
# Добавление пользователя
def add_userx(user_id, user_login, user_name, user_surname):
    with sqlite3.connect(database_path) as con:
        con.row_factory = dict_factory
        con.execute("INSERT INTO storage_users "
                    "(user_id, user_login, user_name, user_surname, user_date, user_unix) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    [user_id, user_login, user_name, user_surname, get_date(), get_unix()])
        con.commit()


# Получение пользователя
def get_userx(**kwargs):
    with sqlite3.connect(database_path) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM storage_users"
        sql, parameters = get_format_args(sql, kwargs)
        return con.execute(sql, parameters).fetchone()


# Получение пользователей
def get_usersx(**kwargs):
    with sqlite3.connect(database_path) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM storage_users"
        sql, parameters = get_format_args(sql, kwargs)
        return con.execute(sql, parameters).fetchall()


# Получение всех пользователей
def get_all_usersx():
    with sqlite3.connect(database_path) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM storage_users"
        return con.execute(sql).fetchall()


# Редактирование пользователя
def update_userx(user_id, **kwargs):
    with sqlite3.connect(database_path) as con:
        con.row_factory = dict_factory
        sql = f"UPDATE storage_users SET"
        sql, parameters = update_format_with_args(sql, kwargs)
        parameters.append(user_id)
        con.execute(sql + "WHERE user_id = ?", parameters)
        con.commit()


# Удаление пользователя
def delete_userx(**kwargs):
    with sqlite3.connect(database_path) as con:
        con.row_factory = dict_factory
        sql = "DELETE FROM storage_users"
        sql, parameters = get_format_args(sql, kwargs)
        con.execute(sql, parameters)
        con.commit()


######################################## СОЗДАНИЕ БАЗЫ ДАННЫХ ######################################
# Создание всех таблиц для Базы Данных
def create_bdx():
    with sqlite3.connect(database_path) as con:
        con.row_factory = dict_factory

        # Таблица с хранением пользователей
        check_sql = con.execute("PRAGMA table_info(storage_users)").fetchall()
        check_create_users = [c for c in check_sql]
        if len(check_create_users) == 7:
            print("DB was found(1/1)")
        else:
            con.execute("CREATE TABLE storage_users("
                        "increment INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "user_id INTEGER, user_login TEXT, user_name TEXT, "
                        "user_surname TEXT, user_date TIMESTAMP, user_unix INTEGER)")
            print("DB was not found(1/1) | Creating...")
        con.commit()
