"""
1.Организовать и вывести последовательность из N случайных целых чисел. Из
исходной последовательности организовать первую последовательность, содержащую
четные числа, и вторую - для всех остальных. Найти среднее арифметическое в полученных
последовательностях.
"""
import random

#Ввод знаения
try:
    a = int(input("кол-во чисел\n\n"))
except ValueError as e:
    print(f"ошибка - {e}")

#начальные значения
start_list = [random.randint(-10, 10) for i in range(a)]
print(start_list, sum(start_list)/len(start_list))

#четные
first_list = [i for i in start_list if i%2 == 0]
print(first_list, sum(first_list)/len(first_list))

#нечетные
second_list = [i for i in start_list if i%2 != 0]
print(second_list, sum(second_list)/len(second_list))