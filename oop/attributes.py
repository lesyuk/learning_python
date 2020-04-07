class Car:
    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1


car_a = Car()
car_a.start("Corrola", "Toyota", 2015)
print(car_a.name)
print(car_a.car_count)
car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.name)
print(car_b.car_count)