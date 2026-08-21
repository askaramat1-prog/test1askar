import sqlite3

from db import queries

path_db = "database/sqlite3.db"


def create_table():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    cursor.execute(queries.create_drinks_table)
    cursor.execute(queries.create_drink_info_table)

    conn.commit()
    conn.close()


def add_product_db(name_drink, price):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    cursor.execute(
        queries.insert_drink,
        (name_drink, price)
    )

    conn.commit()

    drink_id = cursor.lastrowid

    conn.close()

    return drink_id


def add_drink_info_db(drink_id, volume):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    cursor.execute(
        queries.insert_drink_info,
        (drink_id, volume)
    )

    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    cursor.execute(queries.select_drinks_with_info)

    drinks = cursor.fetchall()

    conn.close()

    return drinks