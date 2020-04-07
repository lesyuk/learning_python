class Car:
    message1 = "Двигатель заведен"


    def start(self):
        message2 = "Автомобиль заведен"
        return message2


car_a = Car()
try:
    print(car_a.message2)
except AttributeError:
    print('AttributeError')

print(car_a.message1)