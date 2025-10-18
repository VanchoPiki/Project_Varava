#Вариант 7
#Даны три целых числа: А, В, С. Проверить истинность высказывания: «Число B находится между числами А и С».
#Ввод данных
A, B, C = int(input()), int(input()), int(input())
#Процесс выявления
if A<B<C or A>B>C == True:
    print(f"Число B находится между числами А и C\n {A}, {B}, {C}")
else:
    print("Число B НЕ находится между числами А и C")
#Проверка на ошибки
try:
    A = int(input())
except Exception as e:
    print(f"Произошла ошибка: {e}")

try:
    B = int(input())
except Exception as e:
    print(f"Произошла ошибка: {e}")

try:
    C = int(input())
except Exception as e:
    print(f"Произошла ошибка: {e}")