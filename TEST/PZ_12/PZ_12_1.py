"""Вариант 7.
1. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3"""
import random
a = int(input("Введите размеры квадратной матрицы: "))

#создание самой матрицы 3 на 3

matrix = [[random.randint(1,9) for d in range(a)] for i in range(a)]

for row in matrix:
    print(row)

try:
    n = int(input("\nВведите номер строки N для изменения: "))
    # Перебираем строки с их индексами
    if 1 <= n <= a:
        result_matrix = [
            [val + 3 for val in row] if i == n - 1 else row
            for i, row in enumerate(matrix)
        ]

        print(f"\nМатрица после увеличения строки {n} на 3:")
        for row in result_matrix:
            print(row)

except ValueError as e:
    print(e)