# Python classess and object
# Everything in Python is an object, with its properties and methods.
# A class is like an object constructor, or a blueprint for creating objects

# Example


class MyClass:
    x = 5


p = MyClass()
print(p.x)


# Example The __init__() Method
# all classes have a built-in mehod called __init(), whic is always executed when the class is being initiated.
# __init__() method is used to assign values to object properties. or to perform operations that are neccessary when the object is being created.


# Create a class name Person, use the __init() method to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Mel", 30)

print(f"Hello. my name is {person1.name}. I am {person1.age} years old!")

# Note: __init__ method, you would is called automatically every time the class is being used to create a new object.


# Why use __init__()
# without __init__() method, you would need to set properties manually for each objects
# Example
class PersonWithoutInit:
    pass


p1 = PersonWithoutInit()
p1.name = "Mel"
p1.age = 30

print(p1.name, p1.age)

# Default values in __init__()
# you can also set a default values for parameters in the __init__() method:


class PersonWithDefaultValues:
    def __init__(self, name="Melecio Ceniza", age=50):
        self.name = name
        self.age = age


person2 = PersonWithDefaultValues()

print(f"Helle my name is {person2.name}. I am {person2.age} years old!")


# __init__() in Multiple parameters
class PersonMultipleParameters:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country


personMultiParameters = PersonMultipleParameters(
    "Mel", 30, "Christchurch", "New Zealand"
)

print(
    f"Hello! my name is {personMultiParameters.name}. I am {personMultiParameters.age} years old. I live in {personMultiParameters.city}, {personMultiParameters.country}."
)
