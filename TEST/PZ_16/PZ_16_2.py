"""Создание базового класса "Транспортное средство" и его наследование для создания
классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут общие свойства,
такие как максимальная скорость и количество колес, а классы-наследники будут иметь свои уникальные
свойства и методы."""

class TS:
    def __init__(self, max_speed, wheels_count):
        self.max_speed = max_speed
        self.wheels_count = wheels_count


class Car(TS):
    def __init__(self, max_speed, wheels_count, brand):
        super().__init__(max_speed, wheels_count)
        self.brand = brand


class Motorcycle(TS):
    def __init__(self, max_speed, wheels_count, brand):
        super().__init__(max_speed, wheels_count)
        self.brand = brand


car = Car(max_speed=240, wheels_count=4, brand="Audi")
motorcycle = Motorcycle(max_speed=180, wheels_count=2, brand="Honda")

print("Автомобиль:")
print(f"Максимальная скорость: {car.max_speed}")
print(f"Количество колес: {car.wheels_count}")
print(f"Марка: {car.brand}")

print("\nМотоцикл:")
print(f"Максимальная скорость: {motorcycle.max_speed}")
print(f"Количество колес: {motorcycle.wheels_count}")
print(f"Марка: {motorcycle.brand}")