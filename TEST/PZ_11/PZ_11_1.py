"""
1.Организовать и вывести последовательность из N случайных целых чисел. Из
исходной последовательности организовать первую последовательность, содержащую
четные числа, и вторую - для всех остальных. Найти среднее арифметическое в полученных
последовательностях.
"""

import random
from functools import *

def main():

    a = int(input("Напишите кол-во чисел\n"))

    b = [random.randint(-10, 10) for _ in range(a)]
    print("Сам список", b)

    с = tuple(filter(lambda x: x%2 == 0, b))
    print("Четные: ", с)

    e = tuple(filter(lambda x: x%2 != 0, b))
    print("Нечетные: ", e)

    r = lambda spisok: sum(spisok) / len(spisok) if spisok else 0
    print("Сред. ариф. для чет. -", r(с))
    print("Сред. ариф. для нечет. -", r(e))

main()