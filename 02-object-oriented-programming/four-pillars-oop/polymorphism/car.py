# Python Polymorphism
# Polymorphism word means many forms and in programming it refers to methods/funtion/operators with the same name that can be executed on many objects or classes

# Function Polymorphism
# an example of a python function that can be used on different objects is the len() function

# String
# For strings len() return the number of characters

# Example
x = "Helle World!"
print(len(x))  # output: 12

# Tuple
# For tuples len() returns the number of items in the tuple
# Example
mytuple = ("apple", "banna", "cherry")
print(len(mytuple))  # output : 3

# Dictionary
# For dictionaries len() returns the number of key/value pairs in the directory
# Example
dictionaries = {"brand": "Ford", "model": "Mustang", "year": 1989}
print(len(dictionaries))  # output : 3


# Class in Polymorphism
# Polymorphism is often used in class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat and Plane and they will have a mehod called move()
# Example
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeng", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    x.move()

car1.move()
boat1.move()
plane1.move()
