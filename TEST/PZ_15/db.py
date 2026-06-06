import sqlite3

DB_NAME = "pharmacy.db"


def insert_data():
    initial_medicines = [
        ("Аспирин", "Обезболивающее", 50, 250.00, "Германия"),
        ("Парацетамол", "Жаропонижающее", 100, 80.50, "Россия"),
        ("Нурофен", "Обезболивающее", 5, 450.00, "Франция"),
        ("Анальгин", "Обезболивающее", 0, 120.00, "Россия"),
        ("Амоксиклав", "Антибиотик", 12, 850.00, "Австрия"),
        ("Ибупрофен", "Противовоспалительное", 35, 150.00, "Россия"),
        ("Супрастин", "Противоаллергическое", 22, 320.00, "Венгрия"),
        ("Линекс", "Для пищеварения", 18, 680.00, "Словения"),
        ("Кагоцел", "Противовирусное", 40, 490.00, "Россия"),
        ("Терафлю", "Жаропонижающее", 15, 550.00, "Франция")
    ]

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM medicines")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("""
                INSERT INTO medicines (name, usage, quantity, price, country)
                VALUES (?, ?, ?, ?, ?)
            """, initial_medicines)
            conn.commit()