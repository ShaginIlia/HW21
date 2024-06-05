class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    price = '1000000 р.'

    def horse_powers(self):
        return '210 л.с.'


class Nissan(Vehicle, Car):
    def __init__(self):
        super().__init__()
        self.vehicle_type = 'автомобиль'
        self.price = '800000 р.'

    def horse_powers(self):
        return '145 л.с.'


my_car = Nissan()
print(my_car.vehicle_type)
print(my_car.price)
print(my_car.horse_powers())
