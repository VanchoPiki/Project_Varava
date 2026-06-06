"""Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
Добавьте методы для сложения, вычитания и умножения матриц."""

class Matrix:
    def __init__(self, size, data):
        self.size = size
        self.data = data

    def add(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.size)] for i in range(self.size)]
        return Matrix(self.size, result)

    def subtract(self, other):
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.size)] for i in range(self.size)]
        return Matrix(self.size, result)

    def multiply(self, other):
        result = [[0] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(self.size, result)


m1 = Matrix(2, [[1, 2],
                [3, 4]])

m2 = Matrix(2, [[5, 6],
                [7, 8]])

print("Исходная матрица 1:")
for row in m1.data:
    print(row)

print("\nИсходная матрица 2:")
for row in m2.data:
    print(row)

matrix_sum = m1.add(m2)
matrix_sub = m1.subtract(m2)
matrix_mul = m1.multiply(m2)

print("\nРезультат сложения:")
for row in matrix_sum.data:
    print(row)

print("\nРезультат вычитания:")
for row in matrix_sub.data:
    print(row)

print("\nРезультат умножения:")
for row in matrix_mul.data:
    print(row)