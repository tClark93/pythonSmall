class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(self.health)
        return self
class Dog(Animal):
    def __init__(self,name):
        super().__init__(self,name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self,name):
        super().__init__(self,name)
        self.health = 170
    def displayHealth(self):
        print(self.health, "I am dragon!")
        return self
    def fly(self):
        self.health -= 5
        return self
class Cat(Animal):
    def __init__(self,name):
        super().__init__(self,name)
        self.health = 100
    def sit(self):
        self.health += 5
        return self
animal_1 = Dog("Waffles")
animal_2 = Dragon("Aunt Jemima")
animal_3 = Cat("Kitty")
animal_1.walk().run().run().pet().displayHealth()
animal_2.run().fly().fly().displayHealth()
animal_3.sit().sit().sit().sit().sit().displayHealth()
