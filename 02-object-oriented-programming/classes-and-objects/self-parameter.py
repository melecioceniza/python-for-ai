# Python self Parameter
# The self paraameter
# self parameter is a reference to the current instance of the class
# it is used to access properties and methods that belong to the class

# Example
# use self to access class properties


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is  {self.name}. I am {self.age} years old.")


person = Person("Mel", 30)

person.greet()


# Note: without self, python would not know which object's properties you want to access.
# self parameter links the method to the specific object
# Example
class Person1:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)


p1 = Person1("Mel")

p1.printname()


# Class Properties vs Object Properties
# Properties define inside __init__() belong to each object (instance properties)
# Properties define outside methods belong to the class itself(class properties) and are shared by all objects
# Example
class Person4:
    species = "Human"  # class property

    def __init__(self, name):
        self.name = name  # Instance property


p1 = Person4("Mel")
p2 = Person4("Azinec")

print(p1.name)
print(p2.name)


# Accessing multiple properties
# Class Properties - are variable that belongs to a class. They store data for each object created from the class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()


# Example
# call one method from another method using self:


class Person3:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

    def welcome(self):
        message = self.greet()
        print(f"{message} Welcome to our website!.")


person3 = Person3("Mel")
person3.welcome()

# Code Challenge
# Create a class called Car
# Add an __init__ method with a brand parameter, and store it as a property
# Add a method called show that prints the brand
# Create an object c1 of the Car class with brand "Ford"
# Call the show method on c1
##################################################


class Car:
    def __init__(self, brand):
        self.brand = brand

    def showCar(self):
        print(f"{self.brand}")


car = Car("Ferari")
car.showCar()


##################################################
# Code Challenge
# Create a class called Dog
# Add an __init__() method with parameters name and age and store them as properties using self
# Add a method called bark that prints the dog's name followd by "Woof"
# Create an object d1 of the dog class with the name "Buddy" and age 3
# Call the bark method on d1


class Dog:
    def __init__(self, name="Buddy", age="3"):
        self.name = name
        self.age = age

    def bark(self):
        return f"My dog {self.name} say Woof woof"


d1 = Dog()

print(f"{d1.bark()}")
