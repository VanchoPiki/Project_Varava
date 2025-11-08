"""Найти сумму чисел ряда 1,2,3,4,... от числа п до числа т. Суммирование оформить
функцией с параметрами. Значения п и т программа должна запрашивать."""
# Сама функция

def main(n,m):
    t=0
    while n<m:
        n += 1
        t += n
    return t
#Проверка
try:
    n,m = int(input("Ввeдите первое число\n")), int(input("Введите второе число\n"))
    print(main(n, m))
except ValueError or NameError as e:
    print(e)
