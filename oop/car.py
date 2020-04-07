# Создаем класс Car
class Car:
    # создаем атрибуты класса
    name = "c200"
    make = "mercedez"
    model = 2008

    # создаем методы класса
    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Отключаем двигатель")


# Создаем объект класса Car под названием car_a
car_a = Car()

# Создаем объект класса Car под названием car_b
car_b = Car()

# Тип объекта car_b — класс Car
print(type(car_b))

car_b.start()
print(car_b.model)

print(dir(car_b)) # все атрибуты и методы объекта

