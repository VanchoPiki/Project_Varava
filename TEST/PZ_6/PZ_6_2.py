"""Дан список размера N. Найти минимальный из его локальных максимумов
(локальный минимум — это элемент, который меньше любого из своих соседей)."""
#Импортирую нужную библиотеку
import random
#Ввод нужных значений
try:
    a = int(input("Введите желаемую длину списка\n"))
    c = [random.randint(-100, 100) for _ in range(a)]
    b = a - 1
except ValueError or NameError as e:
    print(e)

t = 0
maxi = []

#Перебор для нахождения локальных максимумов
try:
    for i in range(1, b):
        if c[i] > c[i-1]:
            if c[i] > c[i+1]:
                maxi.append(c[i])
except NameError or ValueError as e:
    print(e)

#Вывод списков
try:
    print(f"\nНачальный список:   {c}\n")
    print(f"Минимальное(-ые) в локальных максимумах:    {min(maxi)}")
except NameError or ValueError as e:
    print(e)