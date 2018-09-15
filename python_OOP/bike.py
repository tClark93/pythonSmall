class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print("You're bike is worth", self.price, "can go up to", self.max_speed, "MPH and has", self.miles, "miles.")
        return self
    def ride(self):
        self.miles += 10
        print("riding")
        return self
    def reverse(self):
        if self.miles <= 0:
           return self
        else:
           print("reversing")
           self.miles -= 5
           return self
    
bike_1 = Bike(500, 10, 0)
bike_2 = Bike(400, 15,100)
bike_3 = Bike(100, 7, 10000)

bike_1.ride().ride().ride().reverse().displayInfo()
print()
bike_2.ride().ride().reverse().reverse().displayInfo()
print()
bike_3.reverse().reverse().reverse().displayInfo()

