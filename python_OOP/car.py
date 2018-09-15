class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def displayInfo(self):
        print("Price:", self.price)
        print("Speed:", self.speed)
        print("Fuel:", self.fuel)
        print("Mileage:", self.mileage)
        return self
    def taxRate(self):
        if self.price > 10000:
            print("Tax: 0.15")
            return self
        else:
            print("Tax: 0.12")
            return self
car_1 = Car(2000, "35mph", "Full", "15mpg")
car_2 = Car(4000, "5mph", "Not Full", "105mpg")
car_3 = Car(6000, "15mph", "Kind of Full", "95mpg")
car_4 = Car(8000, "25mph", "Full", "25mpg")
car_5 = Car(10000, "45mph", "Empty", "25mpg")
car_6 = Car(12000, "35mph", "Empty", "15mpg")

car_1.displayInfo().taxRate()
print()
car_2.displayInfo().taxRate()
print()
car_3.displayInfo().taxRate()
print()
car_4.displayInfo().taxRate()
print()
car_5.displayInfo().taxRate()
print()
car_6.displayInfo().taxRate()
print()