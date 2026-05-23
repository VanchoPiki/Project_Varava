import re


def main():
    file_path = 'Dostoevsky.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        #шаблон ищет 4 цифры подряд
        year_pattern = r'\b\d{4}(?:\s*(?:гг\.|г\.|год[ау]?))\b|\b\d{4}\b'

        #находим все совпадения
        years = re.findall(year_pattern, content)

        #вывод результатов
        print(f"Найдено элементов: {len(years)}")
        print("Список найденных годов:")
        print(years)

    except FileNotFoundError as e:
        print(e)

main()