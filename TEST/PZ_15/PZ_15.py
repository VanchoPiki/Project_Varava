import sqlite3
from db import insert_data

DB_NAME = "pharmacy.db"


def main(title, rows):
    print(f"\n{title}:")
    for row in rows:
        print(row)


with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            usage TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            country TEXT NOT NULL
        )
    """)

insert_data()

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicines")
    main("Исходное состояние базы данных", cursor.fetchall())

    cursor.execute("SELECT * FROM medicines WHERE country = 'Германия'")
    main("Поиск препаратов из страны 'Германия'", cursor.fetchall())

    cursor.execute("SELECT * FROM medicines WHERE price <= 500 AND quantity > 10")
    main("Поиск препаратов дешевле 500 руб. и в количестве > 10 шт.", cursor.fetchall())

    cursor.execute("SELECT * FROM medicines WHERE name LIKE 'А%'")
    main("Поиск препаратов, название которых начинается на 'А'", cursor.fetchall())

    cursor.execute("UPDATE medicines SET price = 1250.50 WHERE id = 2")
    cursor.execute("UPDATE medicines SET price = price * 1.1 WHERE country = 'Франция'")
    cursor.execute("UPDATE medicines SET quantity = quantity - 2 WHERE id = 3 AND quantity >= 2")
    conn.commit()

    cursor.execute("SELECT * FROM medicines")
    main("Состояние базы данных после операций редактирования", cursor.fetchall())

    cursor.execute("DELETE FROM medicines WHERE id = 1")
    cursor.execute("DELETE FROM medicines WHERE quantity = 0")
    conn.commit()

    cursor.execute("SELECT * FROM medicines")
    main("Состояние базы данных после операций удаления", cursor.fetchall())