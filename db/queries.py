create_drinks_table = """
CREATE TABLE IF NOT EXISTS drinks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_drink TEXT NOT NULL,
    price INTEGER NOT NULL
);
"""

insert_drink = """
INSERT INTO drinks(name_drink, price)
VALUES (?, ?);
"""

select_drink = """SELECT * FROM drinks;"""