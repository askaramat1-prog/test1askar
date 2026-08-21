create_drinks_table = """
CREATE TABLE IF NOT EXISTS drinks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL
)
"""


create_drink_info_table = """
CREATE TABLE IF NOT EXISTS drink_info(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink_id INTEGER NOT NULL,
    volume INTEGER NOT NULL,
    FOREIGN KEY (drink_id) REFERENCES drinks(id)
)
"""


insert_drink = """
INSERT INTO drinks(name, price)
VALUES (?, ?)
"""


insert_drink_info = """
INSERT INTO drink_info(drink_id, volume)
VALUES (?, ?)
"""


select_drinks_with_info = """
SELECT drinks.name, drinks.price, drink_info.volume
FROM drinks
INNER JOIN drink_info
ON drinks.id = drink_info.drink_id
"""