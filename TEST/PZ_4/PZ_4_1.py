#Даны два целых числа А и В (А < Б). Найти произведение всех целых чисел от А до В включительно.
#Ввод значений
A, B = int(input()), int(input())
#Нужная переменаая
t = 0
#Цикл
while B>A:
    A += 1
    t += A
print(t)
#Вывод ошибок
try:
    A, B = int(input()), int(input())
except Exception as e:
    print(f"Произошла ошибка: {e}")
try:
    B > A or A == A + 1 or t == t + A
except Exception as e:
    print(f"Произошла ошибка: {e}")