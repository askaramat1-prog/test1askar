import sqlite3
from db import queries

path_db = "database/sqlite3.db"

async def create_table():
    conn  = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_drinks_table)
    conn.commit()
    conn.close()

async def add_product_db(name_drink, price):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_drink, (name_drink, price))
    conn.commit()
    conn.close()

async def get_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_drink)
    drinks = cursor.fetchall()
    conn.close()
    return drinks