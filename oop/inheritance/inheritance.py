# Создание класса Vehicle
class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


# Создание класса Car, который наследует Vehicle
class Car(Vehicle):
    def car_method(self):
        print("Это метод из дочернего класса")


car_a = Car()
car_a.vehicle_method() # Вызываем метод родительского класса