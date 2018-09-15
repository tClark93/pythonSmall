class Product:
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self):
        self.price = round(1.08 * self.price,2)
        return self
    def returnItem(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        if reason == "like new":
            self.status = "for sale"
            return self
        if reason == "opened":
            self.status = "used"
            self.price = round(self.price * .8,2)
            return self
    def displayInfo(self):
        print("Price:", self.price)
        print("Name:", self.name)
        print("Weight:", self.weight)
        print("Brand:", self.brand)
        print("Status:", self.status)
        return self
product_1 = Product(234, "Television", "5 lbs", "LG")
product_2 = Product(89, "Blowdryer", ".5 lb", "Dyson")
product_3 = Product(23, "Mirror", "1lb", "Walmart")
product_4 = Product(889, "Bedframe", "200 lbs", "Ikea")
product_5 = Product(132, "Suitcase", "8lbs", "Griffin")
product_6 = Product(15, "Toothbrush", ".1 lbs", "Oral-B")

product_1.returnItem("defective").addTax().displayInfo()
print()
product_2.addTax().displayInfo()
print()
product_3.addTax().displayInfo()
print()
product_4.addTax().displayInfo()
print()
product_5.addTax().displayInfo()
print()
product_6.returnItem("opened").addTax().displayInfo()
print()