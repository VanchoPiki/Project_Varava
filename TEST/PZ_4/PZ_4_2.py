#Первый день
first_day = 10
#Ввод процента для дальнейших высчитываний
P = float(input("Введите, на сколько процентов лыжник увеличивает дистанцию (от 0 до 50)\n"))
#Высчитывание
while 0<first_day<200:
    first_day += first_day + ((P * first_day) / 100)
    if first_day > 200:
        while first_day < 200:
            first_day -= first_day - ((P * first_day) / 100)
            print(first_day)
    else:
        print(first_day)

try:
    P < 50 or P > 50
except Exception as e:
    print(f"Произошла ошибка: {e}")
