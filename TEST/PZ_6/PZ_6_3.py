"""Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть числа,
 меньшие своих соседей)."""
import random
try:
    a = int(input("Введите желаемую длину списка\n"))
    c = [random.randint(-100, 100) for _ in range(a)]
    y = a - 1
except ValueError or NameError as e:
    print(e)

maxi = []
b = []

try:
    for i in range(1, y):
        if c[i] < c[i - 1]:
            if c[i] < c[i + 1]:
                maxi.append(c[i])
except NameError as e:
    print(e)

for i in maxi:
    i = i**2
    b.append(i)
try:
    print(f"\nСам список:     {c}\n")
    print(f"Локальные минимумы:     {maxi}\n")
    print(f"Возведение в квадрат локальных минимумов:   {b}\n")
except NameError as e:
    print(e)