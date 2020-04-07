class Car:

    # создание методов класса
    def __str__(self): # переопределение метода __str__
        return "Car class Object"


    def start(self):
        print("Двигатель заведен")


car_a = Car()
print(car_a)
# если распечатать без переопределения метода, то выведется <__main__.Car object at 0x000001CCCF4335C0>,
# где 0x000001CCCF4335C0 — номер объекта в памяти
