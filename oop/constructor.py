# Конструктор — это специальный метод, который вызывается по умолчанию когда вы создаете объект класса.

class Car:
    # создание атрибутов класса
    car_count = 0

    # создание методов класса
    def __init__(self):
        Car.car_count += 1
        print(Car.car_count)


car_a = Car()
car_b = Car()
car_c = Car()
