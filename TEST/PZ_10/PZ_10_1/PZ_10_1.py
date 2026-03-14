"""1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:

Исходные данные:
Количество элементов:
Среднее арифметическое элементов:
Положительные четные элементы:
Сумма положительных четных элементов:
Среднее арифметическое положительных четных элементов:"""

try:
    #Список где будут храниться числа
    list=[]
    #Получим список из файла
    with open ("text1.txt", "r", encoding="utf-8") as f:
        for i in f.read().split(","):
            list.append(int(i))
    #кол-во элементов
    num_elemnt = len(list)
    #срд.ариф
    arithmetic_mean_0 = round(sum(list) / len(list), 2)
    #положительные числа
    list_positiv = [i for i in list if i>0 and i%2==0]
    #сумма полож
    sum_positiv = sum(list_positiv)
    #срд.ариф.чет
    arithmetic_mean = round(sum_positiv / len(list_positiv), 2)

    with open("text2.txt", "w", encoding="utf-8") as f:
        f.write(f"кол-во элементов: {num_elemnt}\n\n"
                f"срд.ариф: {arithmetic_mean_0}\n\n"
                f"положительные числа: {list_positiv}\n\n"
                f"сумма полож: {sum_positiv}\n\n"
                f"срд.ариф.чет: {arithmetic_mean}\n\n"
                f"исходные данные : {list}")
except ValueError as e:
    print(f"Произошла ошибка: {e}")