class Vehicle:
    def __init__(self, wheels, seats, engin):
        self.wheels = wheels
        self.seats = seats
        self.engin = engin

    def v_wheels(self):
        print(f'The Vehicle is having {self.wheels}')

    def v_seats(self):
        print(f'The vehicle is having {self.seats}')

    def v_engin(self):
        print(f'The vehicle is having {self.engin} cc engin')

    def v_vehicle_details(self):
        print(f'The vehicle is having {self.wheels}, {self.seats} seats for passengers and engine of {self.engin} cc')


class Bus(Vehicle):
    def __init__(self, wheels, seats, engin):
        Vehicle.__init__(self, wheels, seats, engin)


v = Vehicle(4, 34, 1200)
b = Bus(4, 40, 3000)
v.v_wheels()
v.v_vehicle_details()