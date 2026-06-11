# Inheritance Class in Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?
# Yes, if we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

# Example
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"The {self.brand} {self.model} is now moving!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print(f"The {self.brand} {self.model} is now sailing!")


class Plane(Vehicle):
    def move(self):
        print(f"The {self.brand} {self.model} is now flying!")


car1 = Car("Toyota", "Camry")
boat1 = Boat("Forester", "Cruiser")
plane1 = Plane("Airbus", "A320")
car1.move()  # output Moving
boat1.move()  # output Toyota
plane1.move()

# Using for loop
for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
# output :
# Toyota
# Camry
# Moving
# Forester
# Cruiser
# Sailing
