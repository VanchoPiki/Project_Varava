"""2. Из предложенного текстового файла (text18-7.txt) вывести
на экран его содержимое, количество букв в нижнем регистре.
Сформировать новый файл, в который поместить текст в стихотворной
форме предварительно поставив последнюю строку между второй и третьей."""

print('\n')
try:
    #вывод стихотворения
    with open("text18-7.txt", "r", encoding="utf-8") as f:
        print(f.read())

    #количество букв в нижнем регистре
    with open("text18-7.txt", "r", encoding="utf-8") as f:
        list = f.readlines()
        t = 0
        for i in list:
            for _ in i:
                if _.islower():
                    t += 1
        print(f"\nколичество букв в нижнем регистре: {t}\n")

    #подстановка строки между второй и третьей
    with open("text18-7.txt", "r", encoding="utf-8") as f:
        list = f.readlines()
        list.insert(2, (list[6] + "\n"))
        list.pop()
        with open("text2.txt", "w", encoding="utf-8") as f:
            f.writelines(list)
except TypeError as e:
    print(f"Произошла ошибка - {e}")