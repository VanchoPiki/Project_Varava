"""Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
Добавьте методы для сложения, вычитания и умножения матриц."""

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def plus(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def minus(self, other):
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def multi(self, other):
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)


m1 = Matrix([[2, 2],
             [3, 6]])

m2 = Matrix([[4, 6],
             [7, 9]])

print("Исходная матрица 1:")
for row in m1.data:
    print(row)
print(f"Размер: {m1.rows}x{m1.cols}")

print("\nИсходная матрица 2:")
for row in m2.data:
    print(row)
print(f"Размер: {m2.rows}x{m2.cols}")

matrix_sum = m1.plus(m2)
matrix_sub = m1.minus(m2)
matrix_mul = m1.multi(m2)

print("\nРезультат сложения:")
for row in matrix_sum.data:
    print(row)

print("\nРезультат вычитания:")
for row in matrix_sub.data:
    print(row)

print("\nРезультат умножения:")
for row in matrix_mul.data:
    print(row)