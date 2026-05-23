"""2. В матрице элементы последнего столбца заменить на -1."""
a = int(input("Введите размеры квадратной матрицы: "))
#создание самой матрицы 3 на 3
matrix = [[int(x) for x in input(f"Введите строку {i} через пробел: ").split()] for i in range(a)]

print(f"\nМатрица начальная")
for row in matrix:
    print(row)

try:
    # matrix — наша исходная матрица
    result_matrix = [row[:-1] + [-1] for row in matrix]

    print(f"\nМатрица после замены последнего столбца на '-1':")
    for row in result_matrix:
        print(row)

except ValueError as e:
    print(e)