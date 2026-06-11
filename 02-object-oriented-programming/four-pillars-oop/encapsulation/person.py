# Python Encapsulation
# Encapsulation is about protecting data inside a class
# it means keeping data (properties) and methods togethere in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.


# Private Properties
# in Python, you can make properties private by using a double underscore
# Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private property


p1 = Person("Mel", 30)
print(p1.name)
# print(p1.__age)  # This will cause an error

# Note: Private properties cannot be accessed directly from outside the class


# Get Private Property Value
# To access a private proper
# Use a getter method to access a private property
class PersonGet:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


person1 = PersonGet("Mel", 30)
print(person1.get_age())

# Set Private Property Value
# To modify a private property, you can create a setter method
# The setter method can also validate the value before setting it


# Example
# Use a setter method to change a private property
class PersonSet:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")


# instatniate object
personset = PersonSet("Mel", 30)

# call the get_age() method
print(personset.get_age())

# Set the age = 26
personset.set_age(26)

# Get the age from set_age() method
print(personset.get_age())
