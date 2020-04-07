class Car:
    def __init__(self):
        print ("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999


car_a = Car()
print(car_a.name)
try:
    print(car_a.make)
except AttributeError:
    print('AttributeError')